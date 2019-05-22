# CryptoPad
Note Pad Editor that can Encrypt or Decrypt Text combined with a Reverse Shell.

# Instructions
1. You can test the CryptoPad Reverse Shell Application locally, meaning that the Server.py and the CryptoPad.py are run on the same computer.\
  a. You do not need to change the IP address in the Client.py if you are testing the application locally on the same computer.\

2. You can test the CryptoPad Reverse Shell Application across a network, meaning that the Server.py is run on one computer and the CryptoPad.py is run on another computer.\
  a. The IP address in the Client.py needs to be changed to match the IPV4 IP address of the computer running the Server.py.
  b. You need to bundle the CryptoPad.py, Client.py and the VernamCipher.py together on the Client computer in the same folder location.

4. To test the Reverse Shell Application, open and run the Server.py.\ 
  a. Make sure you have changed the IP address in the Client.py to match the IPV4 IP address of the computer running the Server.py
  b. The Server comes with a few commands that are used to connect to a client.
  	1. list - The lists command will display the different clients connected to the Server.
  	2. select i - This command allows you to select a specific Client to Connect with. Where i is the Client ID.
  	3. quit - To close the connection between the Server and the Client.

3. To test the CryptoPad Application, open and run the CryptoPad.py\
  a. Make sure that the CryptoPad.py, Client.py and the VernamCipher.py are in the same folder location.

# Important
This is program is only intended for educational use and I am not responsible for any illegal actions you do with it.
You can find the YouTube Tutorials of how to make your own Python Reverse Shell at the link below.\
https://www.youtube.com/playlist?list=PL6gx4Cwl9DGCbpkBEMiCaiu_3OL-_Bz_8
