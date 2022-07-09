# Data Visualization of key exchange of WPA2

## Introduction

### 4-Way Handshake

![image1.png](image1.png)

#### MSK-Master Session Key ( or AAA Key):
Key information that is jointly negotiated between the Supplicant & Authentication Server. This key information is transported via a secure channel from Authenticating Server to Authenticator.

#### PMK-Pairwise Master Key:
PMK is derived from MSK seeding material. PMK is first 256bits (0-255) of MSK. It can be derived from an EAP method or directly from a PresharedKey(PSK).

#### GMK-Group Master Key:
GMK is randomly created on Authenticator & refresh it in configured time interval to reduce the risk of GMK being compromised.

#### PTK-Pairwise Transient Key:
A value derived from PMK,Authenicator nonce(Anonce),Supplicant nonce(Snonce), Authenticator Address, Supplicant Address. This is used to encrypt all unicast transmission between client & an AP. PTK consist of 5 different keys

1. KCK-Key Confirmation Key-used to provide data integrity during 4 -Way Handshake & Group Key Handshake.
2. KEK – Key Encryption Key– used by EAPOL-Key frames to provide data privacy during 4-Way Handshake & Group Key Handshake.
3. Temporal Key – used to encrypt & decrypt MSDU of 802.11 data frames between supplicant & authenticator
4. Temporal MIC-1
5. Temporal MIC-2

#### GTK-Group Temporal Key:
GTK is used to encrypt all broadcast/multicast transmission between an AP & multiple client statsions. GTK is derived on Authenticator & sending to supplicant during 4-Way Handshake (M3)

4-Way handshake utilizing EAPOL-Key frames initiated by the Authenticator to do the following.
1. Confirm that live peer holds PMK
2. Confirm that PMK is current.
3. Derive a fresh PTK from PMK & Install the pairwise encryption & integrity keys into 802.11
4. Transport the GTK & GTK sequence number from Authenticator to Supplicant & install them in Supplicant & AP(if not already installed)
5. Confirm cipher suite selection.


Below figure shows the steps involved in 4-Way handshake process.

![image2.png](image2.png)

#### Below Python Code visualize the packets captured:


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv(r"C:\Users\JUNE\Desktop\CISCO_PROJECT_SIP_WPA2\CISCO_PROJECT_WPA2_PROTOCOL\capture.csv")
```


```python
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>No.</th>
      <th>Time</th>
      <th>Source</th>
      <th>Destination</th>
      <th>Protocol</th>
      <th>Length</th>
      <th>Info</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0.000000</td>
      <td>fa:d8:66:5d:ab:75</td>
      <td>Broadcast</td>
      <td>802.11</td>
      <td>206</td>
      <td>Beacon frame, SN=385, FN=0, Flags=........, BI...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>0.236096</td>
      <td>NaN</td>
      <td>XiaomiCo_ca:54:b1 (b4:c4:fc:ca:54:b1) (RA)</td>
      <td>802.11</td>
      <td>10</td>
      <td>Clear-to-send, Flags=........</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>0.289811</td>
      <td>NaN</td>
      <td>5a:56:22:c0:f3:de (5a:56:22:c0:f3:de) (RA)</td>
      <td>802.11</td>
      <td>10</td>
      <td>Acknowledgement, Flags=........</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>0.599594</td>
      <td>NaN</td>
      <td>AzureWav_67:70:77 (80:91:33:67:70:77) (RA)</td>
      <td>802.11</td>
      <td>10</td>
      <td>Acknowledgement, Flags=........</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>0.599598</td>
      <td>NaN</td>
      <td>82:f2:1d:7a:22:fa (82:f2:1d:7a:22:fa) (RA)</td>
      <td>802.11</td>
      <td>10</td>
      <td>Acknowledgement, Flags=........</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>4120</th>
      <td>4121</td>
      <td>137.702509</td>
      <td>NaN</td>
      <td>AzureWav_67:70:77 (80:91:33:67:70:77) (RA)</td>
      <td>802.11</td>
      <td>10</td>
      <td>Acknowledgement, Flags=........</td>
    </tr>
    <tr>
      <th>4121</th>
      <td>4122</td>
      <td>137.740377</td>
      <td>3e:39:40:0b:1b:2d (3e:39:40:0b:1b:2d) (TA)</td>
      <td>IntelCor_22:0f:a6 (5c:e0:c5:22:0f:a6) (RA)</td>
      <td>802.11</td>
      <td>20</td>
      <td>802.11 Block Ack Req, Flags=........</td>
    </tr>
    <tr>
      <th>4122</th>
      <td>4123</td>
      <td>137.743952</td>
      <td>IntelCor_22:0f:a6 (5c:e0:c5:22:0f:a6) (TA)</td>
      <td>3e:39:40:0b:1b:2d (3e:39:40:0b:1b:2d) (RA)</td>
      <td>802.11</td>
      <td>28</td>
      <td>802.11 Block Ack, Flags=........</td>
    </tr>
    <tr>
      <th>4123</th>
      <td>4124</td>
      <td>137.743954</td>
      <td>3e:39:40:0b:1b:2d (3e:39:40:0b:1b:2d) (TA)</td>
      <td>IntelCor_22:0f:a6 (5c:e0:c5:22:0f:a6) (RA)</td>
      <td>802.11</td>
      <td>16</td>
      <td>Request-to-send, Flags=........</td>
    </tr>
    <tr>
      <th>4124</th>
      <td>4125</td>
      <td>137.743952</td>
      <td>NaN</td>
      <td>3e:39:40:0b:1b:2d (3e:39:40:0b:1b:2d) (RA)</td>
      <td>802.11</td>
      <td>10</td>
      <td>Clear-to-send, Flags=........</td>
    </tr>
  </tbody>
</table>
<p>4125 rows × 7 columns</p>
</div>




```python
data=data[data["Protocol"]=="EAPOL"]
data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>No.</th>
      <th>Time</th>
      <th>Source</th>
      <th>Destination</th>
      <th>Protocol</th>
      <th>Length</th>
      <th>Info</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>746</th>
      <td>747</td>
      <td>34.323128</td>
      <td>fa:d8:66:5d:ab:75</td>
      <td>CloudNet_8a:10:fd</td>
      <td>EAPOL</td>
      <td>133</td>
      <td>Key (Message 1 of 4)</td>
    </tr>
    <tr>
      <th>748</th>
      <td>749</td>
      <td>34.326202</td>
      <td>CloudNet_8a:10:fd</td>
      <td>fa:d8:66:5d:ab:75</td>
      <td>EAPOL</td>
      <td>155</td>
      <td>Key (Message 2 of 4)</td>
    </tr>
    <tr>
      <th>751</th>
      <td>752</td>
      <td>34.331832</td>
      <td>fa:d8:66:5d:ab:75</td>
      <td>CloudNet_8a:10:fd</td>
      <td>EAPOL</td>
      <td>189</td>
      <td>Key (Message 3 of 4)</td>
    </tr>
    <tr>
      <th>753</th>
      <td>754</td>
      <td>34.335419</td>
      <td>CloudNet_8a:10:fd</td>
      <td>fa:d8:66:5d:ab:75</td>
      <td>EAPOL</td>
      <td>133</td>
      <td>Key (Message 4 of 4)</td>
    </tr>
  </tbody>
</table>
</div>




```python
source=set(data["Source"])
source=list(source)
router='fa:d8:66:5d:ab:75'
source.remove(router)
router='\033[1m'+router
print("\033[1;31;47m")
print(f"Source-{router}")
print(f"\n{len(source)}-Clients")
l=len(source)
np_array=np.array(source)
reshaped_array=np.reshape(np_array, (l,1))
a_dataframe=pd.DataFrame(reshaped_array, columns=["Clients"])
a_dataframe
```

    [1;31;47m
    Source-[1mfa:d8:66:5d:ab:75
    
    1-Clients
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Clients</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>CloudNet_8a:10:fd</td>
    </tr>
  </tbody>
</table>
</div>




```python
print('\033[1m'+'4-way handshake')
result=[]
count=0
for i in source:
    message = data[data["Source"]==i]
    message=len(set(message["Info"]))
    if(message==2):
        result.append(100)
    else:
        result.append(0)
width =.35
m1_t = pd.DataFrame({
    'capture':result
})
m1_t[['capture']].plot(kind='bar',width=width)
ax=plt.gca()
device=[i for i in source]
ax.set_xticklabels((source))
plt.show()
print(f"{result.count(100)}-Successful")
print(f"{result.count(0)}-UnSuccessful")
```

    [1m4-way handshake
    


    
![png](output_5_1.png)
    


    1-Successful
    0-UnSuccessful
    

## Results

##### Message 1 (M1)
* Authenticator sends EAPOL-Key frame containing an ANonce(Authenticator nonce) to supplicant.
* With this information, supplicant have all  necessary input to generate PTK using pseudo-random function(PRF)

![messagem1.png](messagem1.png)

##### Message 2 (M2)
* Supplicant sends an EAPOL-Key frame containing SNonce to the Authenticator.
* Now authenticator has all the inputs to create PTK.
* Supplicant also sent RSN IE capabilities to Authenticator & MIC
* Authenticator derive PTK & validate the MIC as well.

![messagem2.png](messagem2.png)

##### Message 3 (M3)
* If necessary, Authenticator will derive GTK from GMK.
* Authenticator sends EAPOL-Key frame containing ANonce, RSN-IE & a MIC.
* GTK will be delivered (encrypted with PTK) to supplicant.
* Message to supplicant to install temporal keys.

![messagem3.png](messagem3.png)

##### Message 4 (M4)
* Supplicant sends final EAPOL-Key frame to authenticator to confirm temporal keys have been installed.

![messagem4.png](messagem4.png)

##### Ladder Diagram
* The ladder diagram is generated using wireshark flowgraph tool 

![ladderdiagram](ladderdiagram.png)
