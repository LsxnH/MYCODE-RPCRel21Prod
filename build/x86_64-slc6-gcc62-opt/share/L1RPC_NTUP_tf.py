#!/usr/bin/env python

#########################################################################
##
## Simple transformation template satisfying Tier-0 system requirements
##
##  - input parameter: file containing a json dictionary consisting of the key/value pairs
##     1) a) 'inputFiles': python list
##           ['datasetname#filename1', 'datasetname#filename2', ...] (input dataset + file names)
##        b) 'inputFiles': python list of file dictionaries
##        [{'lfn':'filename1', 'checksum':'checksum1', 'dsn':'datasetname1', 'events': N1, ...},
##         {'lfn':'filename2', 'checksum':'checksum2', 'dsn':'datasetname2', 'events': N2, ...}, ...]
##     2) 'outputFile': string 'datasetname#filename' (output dataset name + file name)
##
##  - runs just print statements - to be replaced by the actual job
##
## (C) Jaroslav Guenther (June 2017), Rustem Ospanov (January 2018)
#########################################################################

import sys, string, commands, os.path, os, json, time, pprint, traceback
import subprocess

#########################################################################
# Utility function
#
def getSubFileMap(fname, nevts=0) :
    if os.path.isfile(fname) :
        sz = os.path.getsize(fname)
        map = { 'name': fname,
                'file_size' : sz,
                'nentries' : nevts,
              }
    else :
        map = {}
    return map

#########################################################################
def runL1MuonJob(jsonfile) :

    tstart = time.time()

    print "\n##################################################################"
    print   "##                  Starting L1 Muon tf                         ##"
    print   "##################################################################\n"

    # initialize exit values
    exitCode = 0
    exitAcronym = 'OK'
    exitMsg = 'trf finished OK'

    # initialize other report variables / due to use of try/except statements needed to be done here
    nfiles = 0
    inputfilelist = []
    inputdsname = ''; inputfilenames = []
    outdsname   = ''; outfilename    = ''

    parmap = {}
    outmap = {}
    # nevts you can set during the execution time or by summing event number from the input file dictionary passed in the json argument file if existing there
    nevts = 0

    try:
        #
        # extract any parameters passed to the job from json file with argument dictionary
        #
        print "Using json file ", jsonfile, " for input parameters."

        if not os.path.isfile(jsonfile):
            exitAcronym = 'ERROR'
            exitMsg = 'Invalid JSON file: %s' %jsonfile
            traceback.print_exc()

        f = open(jsonfile, 'r')
        parmap = json.load(f)
        f.close()

        print "\nFull Tier-0 run options:\n"
        pprint.pprint(parmap)

        inputfilelist = parmap.get('inputFiles', [])
        outdsname   = (parmap['outputFile']).split('#')[0]
        outfilename = (parmap['outputFile']).split('#')[1]

        nfiles = len(inputfilelist)
    except :
        exitCode = 1
        exitAcronym = 'TRF_NOINPUT'
        exitMsg = 'Trouble reading json input dict.'
        print "ERROR: ", exitMsg
        traceback.print_exc()

    #
    # check for problem with job definition - no files
    #
    if exitAcronym == 'OK' and not nfiles :
        exitCode = 2
        exitAcronym = 'TRF_NOINPUT'
        exitMsg = 'Empty input file list.'
        print "ERROR: ", exitMsg

    if exitAcronym == 'OK' :
        try :
            # assemble list of inputfilenames ['filename1', 'filename2', ...]
            if isinstance(inputfilelist[0], unicode) :
                inputdsname = (inputfilelist[0]).split('#')[0]
                for val in inputfilelist :
                    inputfilenames.append(val.split('#')[1])

            elif isinstance(inputfilelist[0], dict) :
                inputdsname = inputfilelist[0]['dsn']
                for fdict in inputfilelist :
                    if fdict.has_key('lfn') :
                        inputfilenames.append(fdict['lfn'])
                    else:
                      exitCode = 3
                      exitAcronym = 'TRF_NOINPUT'
                      exitMsg = 'ERROR: missing lfn in the input file list.'
                      print "ERROR: ", exitMsg
                      break
            else :
                exitCode = 4
                exitAcronym = 'TRF_NOINPUT'
                exitMsg = 'ERROR: unexpected type of the input file list, transform is recognising only unicode or dict.'
                print "ERROR: ", exitMsg

            # checking if input file list is empty
            if exitAcronym == 'OK' and not len(inputfilenames) :
                exitCode = 5
                exitAcronym = 'TRF_NOINPUT'
                exitMsg = 'empty input file list'
                print "ERROR: ", exitMsg
        except :
            exitCode = 6
            exitAcronym = 'TRF_NOINPUT'
            exitMsg = 'Unrecognised error in assembling list of input files'
            print "ERROR: ", exitMsg
            traceback.print_exc()

    if exitAcronym=='OK':
      try :
          # proceed and execute your job
          print "------------------------------------------------------------------"
          print "\nRunning main execution step:"
          print "------------------------------------------------------------------"
          print "on the following files: "
          print inputfilenames
          print "\nwith the following outputs: "
          print "  dataset name: ", outdsname
          print "  file name:    ", outfilename
          print "------------------------------------------------------------------"
          # here you should prepare + run your executable, e.g., 
          #  - assemble your custom jobOption file from the input parameters
          #  - assemble run command: athena <jobOption file> 
          #  - execute run command in os.system or commands.getstatusoutput call
          #  - catch errors, do error categorisation + reporting
          #  - determine nevts
          #  - etc.

          execAthenaScript(inputfilenames, outfilename)

          print "\nMain algorithm execution finished."
          print "------------------------------------------------------------------"

      except :
          exitCode = 7
          exitAcronym = 'TRF_EXEC_ERROR'
          exitMsg = 'problem in the main execution stage of the job.'
          print "\nERROR: ", exitMsg
          traceback.print_exc()

    dt = int(time.time() - tstart)
    print   "\n## ... elapsed time: ", dt, " sec"
    print   "## ... exitCode:     ", exitCode
    print   "## ... exitAcronym:  ", exitAcronym
    print   "## ... exitMsg:      ", exitMsg
    print   "## ... nevts:        ", nevts


    ######################################################################### 
    # get info for jobReport.json file
    #
    outputslist = []

    if exitAcronym == 'OK' :
        fmap1 = getSubFileMap(outfilename, nevts=nevts)
        outputslist.append({'dataset': outdsname, 'subFiles': [fmap1]})

    if not outputslist :
        outputslist = [ {'dataset': '', 'subFiles': []} ]
    
    outmap = { 'exitAcronym': exitAcronym,
               'exitCode': exitCode,
               'exitMsg': exitMsg,
               'files': { 'output' : outputslist },
               'resource': { 'transform': {'processedEvents': long(nevts), 'wallTime':  int(dt)} }
             }

    #########################################################################
    # jobReport.json file creation
    f = open('jobReport.json', 'w')
    json.dump(outmap, f)
    f.close()

    print "\n##################################################################"
    print   "## End of job."
    print   "##################################################################\n"


#########################################################################
def writeFile(fname, text):

   ifile = open(fname, 'w')
   ifile.write(text)
   ifile.close()


#########################################################################
def execAthenaScript(inputfiles, outfile):
    
    #
    # Write text file with input files
    #
    print inputfiles

    efile = 'l1_rpc_ntup_exec.sh'
    ifile = 'l1_rpc_ntup_input.txt'
    ftext = ''

    for f in inputfiles:
        ftext+= '%s\n' %f

    writeFile(ifile, ftext)

    #
    # Prepare athena command 
    #
    jobopt = 'PhysicsRPCProd/readDESD_MCP_PhysicsAnpRPC.py'

    atext  = '#\n# Shell script to execute athena job\n#\n'
    atext += 'athena %s -c "outfile=\'%s\';inputFileList=\'%s\'"\n' %(jobopt, outfile, ifile)
    
    writeFile(efile, atext)

    process = subprocess.Popen(['/bin/bash', efile])
    process.communicate()

    if process.returncode != 0:
        print "Athena job failed with return code: %s" %process.returncode
        sys.exit(-1)

########################################
## main()
########################################
if __name__ == "__main__" :

    if (len(sys.argv) != 2) and (not sys.argv[1].startswith('--argJSON=')) :
        print "Input format wrong --- use "
        print "   --argJSON=<json-dictionary containing input info> with key/value pairs: "
        print "     1) 'inputFiles': python list ['datasetname#filename1'] "
        print "        (input dataset + file names) "
        print "     2) 'outputFile': string 'datasetname#filename' (output dataset name + file) "
        print ""
        sys.exit(-1)

    else :
        jsonfile = sys.argv[1][len('--argJSON='):]
        runL1MuonJob(jsonfile)
