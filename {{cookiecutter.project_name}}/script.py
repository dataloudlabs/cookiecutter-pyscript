import os
import argparse



def main():
    pass



def test_main():
    main()
    assert False


def __parse_args():
    ap = argparse.ArgumentParser()
    #ap.add_argument("--path", required=False, help="Path to recursively look into.")

    args = None
    try:
        args = vars(ap.parse_args())
    except Exception as e:
        ap.print_help()

    # args is a dict with the arguments passed in from the command line
    return args


if __name__ == '__main__':
    work_args = __parse_args()

    main()
