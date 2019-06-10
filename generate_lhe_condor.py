#! /usr/bin/env python

from general_condor_functions import getbasic_parser
from general_condor_functions import create_output_directory
from general_condor_functions import create_jdl_file_for_condor
from general_condor_functions import create_sh_file_for_condor

def getargs():
    parser = getbasic_parser()
    parser.add_argument('-n', '--nevents',
                        default=10000,
                        help='Total number of events to generate.'
                       )
    parser.add_argument('-cpu', '--ncpu',
                        default=8,
                        help='number of cpu to run'
                       )
    parser.add_argument('-r', '--randomnumber',
                        default=11,
                        help='random seed'
                       )
    return parser.parse_args()


def main():
    # get input arguments
    args = getargs()
    print args

    # list of input files to be added in jdl file
    inputlist = "run_mg5_condor.sh"

    # command to run
    command = './runcmsgrid.sh '+str(args.nevents)+' '+str(args.randomnumber)+' '+str(args.ncpu)

    # Get Output directory name
    output_folder, output_log_path = create_output_directory(args)

    # create the jdl file for condor
    create_jdl_file_for_condor(args, inputlist, output_log_path)

    # create the sh file for condor
    create_sh_file_for_condor(args, command, output_folder)

if __name__ == "__main__":
    main()
