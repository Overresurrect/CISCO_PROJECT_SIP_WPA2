import pandas as pd

#Read CSV file
df = pd.read_csv('sipall.csv')

#List all Packets
print('PCAP Data\n')
print(df)


#No of packets
packets = df.shape[0]
print('\nNumber of Packets: ', packets)

#List onlt SIP Packets
sip = df[df['Protocol']=='SIP']
print('SIP Protocol\n', sip)

#List the Info Field
print('\nSIP Packets Info\n', sip[['No.','Time', 'Info']])

#Analysis
infos = sip['Info'].to_list()
print('\nInfo Fields\n')
for info in infos:
    flag =info.split(':')
    print('\n',flag[0])

#Plotting in Matplotlib For length of sip packets
%matplotlib inline
df[df['Protocol']=='SIP'].Length.hist(bins=15)
