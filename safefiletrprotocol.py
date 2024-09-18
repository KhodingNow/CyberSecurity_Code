
import paramiko

# this Python code demos how to use Paramiko libr to establish a secure SFTP (SSH File Trans Prot) connection & download a file from a remote server.

hostname = 'user.com'
port = 22
username = 'you_username'
password = 'pssword_123'
remote_file_path = '/path/to/remote/file.txt'
local_file_path = 'local_file.txt'

# code above defines various parameters for the SFTP connection and their use

try:
    # Create an SSH client instance
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # the line above sets the host key policy to automatically add the remote
    #..server's host key to the local known_host file. This is neccessary for the first-time connection to  a server

    # Connect to the SSH server

    ssh.connect(hostname, port, password)

    sftp = ssh.open_sftp()

    # after connecting via SSH, the code creates as SFTP session ('sftp') using the SSH
    #..connection. This allows for secure file transfer operations

    #Download the remote file securely
    sftp.get(remote_file_path, local_file_path)

    #the above line uses 'sftp.get()' method to download the remote file ('remote_file_path'), saves it locally
    #...with the specified filename ('local-file_path')


    # Close the SFTP session connection
    sftp.close()
    ssh.close()

    print(f"Successfully downloaded {remote_file_path} to {local_file_path}")
except Exception as e:
    print(f"Error: {str(e)}")

# The 'try' block wraps the entire process, including connecting, transferring the file, and closing the connections. 
# If any exceptions occur during these operations, they are caught, an error message is printed
#  