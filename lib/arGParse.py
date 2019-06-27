import argparse

def _argparse():
    parser = argparse.ArgumentParser(description='Docx 批量搜索工具.')
    parser.add_argument('--version','-v',action='store_true',help='查看版本.')
    # parser.add_argument('--sFtp_config','-sftp',action='store_true',help='配置sftp服务器.')
    parser.add_argument('--path','-p',help='输入路径.')

    args = parser.parse_args()

    return args


    