import re
import string


msg_1 = '''ILOOO ZEWPG CCHPQ!
ERKPFDGH:
    TBZQ-WKREEA-FAYC
    CHX-CJVYUK-VWYP
    PPRRSMD
    

I don't understand you

NGJPQ QGHSR UMPEK!
SXXWNZQW:
    YYNO-PWJKUQ-LJQU
    MPB-UOIVMZ-UMCP
    COGIIVD
    

I don't understand you

NPWSH RQPDV YEZEZ!
VRFDJNOP:
    RDII-JHNDJY-UMKY
    EZC-HXOOKX-QTAY
    EQMNGDZ
    

I don't understand you

MHRDI PCZXO GDLQX!
FGBBAIIJ:
    XVXH-JPNSOB-JPZG
    DLM-SDADWK-GCQV
    MHQFNRA
    

I don't understand you

GMAXS YPLOU SFGXK!
BMZYJXHJ:
    FUPV-VZQIXW-RPXS
    FGU-QDAXHX-RUYH
    GIHGBDB
    

I don't understand you

SLMOB JDGJX TWPTX!
AQAKMPVV:
    HMJU-GLIFDB-IYKT
    WPC-RZEWPB-VYBP
    YSPQAVY
    

I don't understand you

ZEXJI MVPWH WVHJB!
CHOXPJUG:
    WKIQ-JGKBDS-NVXW
    VHW-SASKZC-OGWX
    TBOOSED
    

I don't understand you

JUTWG KYHRT FJMCC!
CPVFPIQJ:
    PWWG-OPIWZG-FHBF
    JMY-TBVXLM-USBY
    ZIQIHOV
    

I don't understand you

NJXRX HKMAV NHLBM!
ROYBYWGO:
    JHPR-THDKAW-GPCN
    HLC-YYFIGU-XTSF
    MGHHTXU
    

I don't understand you

BOPAZ DWLME JLEWU!
JQPZVPRT:
    JPEV-LMGOBC-QXMJ
    LEA-RDBLPC-HWGU
    GXIVJRM
    

I don't understand you

UXZMJ ZCEXF APUBC!
NHNAHEVL:
    VZEO-ELEHYX-OYUA
    PUQ-XVAIHW-TFWW
    LZSUHIK
    

I don't understand you

TDLXG RHUTL JFJGW!
NIEOPEOE:
    GLQU-GEULDY-IFCJ
    FJY-FUCFMY-VNCM
    QJBQWJW
    

I don't understand you

FDTTU LPJXU MQOQY!
QSRVXQUG:
    JGXX-WUOKVQ-HUWM
    QOB-HMCOLC-EJXT
    VGIGEIH
    

I don't understand you

CZSXB QJOPJ PPXYC!
IBKYYXXW:
    OPTH-CJVYUK-VWYP
    PXW-WKREEA-FAYC
    CUGRDOP
    

I don't understand you

LAAPT LQXZR PCDQA!
KIFPFTHC:
    THJT-UOIVMZ-UMCP
    CDB-PWJKUQ-LJQU
    MBXVXHZ
    

I don't understand you

ABNZZ BVDLI YEDRQ!
IGMNUJTU:
    LMCV-HXOOKX-QTAY
    EDS-JHNDJY-UMKY
    ETZOFNL
    

I don't understand you

NYHLH CZDTN VMZPY!
DXWEWCVH:
    ELBE-SDADWK-GCQV
    MZG-JPNSOB-JPZG
    DZJUBUG
    

I don't understand you

PDRTM ZOZSF HGADB!
GZMRMBES:
    GEWF-QDAXHX-RUYH
    GAW-VZQIXW-RPXS
    FHGXVHP
    

I don't understand you

QVYSR QHAAG PYBZW!
EJPKTWFQ:
    WUBL-RZEWPB-VYBP
    YBC-GLIFDB-IYKT
    WMUHUWH
    

I don't understand you

OUGAX WHBNQ XTYNB!
UGMFCBLR:
    CJGU-SASKZC-OGWX
    TYX-JGKBDS-NVXW
    VRBTYTM
    


I don't understand you

SMKNR VUYHO YZDIS!
OUIMUGUS:
    UOQJ-TBVXLM-USBY
    ZDY-OPIWZG-FHBF
    JXTVYIL
    
I don't understand you

YKOHG ZVDRI FMVXG!
VBPWYQJT:
    HXYR-YYFIGU-XTSF
    MVQ-THDKAW-GPCN
    HRZELAE
    

I don't understand you

OWPRM AEVYH UGUPW!
ITWMGYRY:
    SDQI-RDBLPC-HWGU
    GUK-LMGOBC-QXMJ
    LGHFSSU
    

I don't understand you

RHSYQ BTUGV WLMJC!
OZDPSQIR:
    QDRN-XVAIHW-TFWW
    LMZ-ELEHYX-OYUA
    PMMLTVJ
    

I don't understand you

ZPDGH TOMKU MQKIX!
AHBMTRNX:
    RZPF-FUCFMY-VNCM
    QKX-GEULDY-IFCJ
    FQRUZEO
    

I don't understand you

YZXKP SSKOQ TVWWY!
AMYIWPFF:
    SADG-HMCOLC-EJXT
    VWK-WUOKVQ-HUWM
    QHXJGXX

'''

msg = """
HELLO FIELD AGENT!
COMMANDS:
    SEND-SECRET-DATA
    GET-SECRET-DATA
    GOODBYE
    """


def reformat(msg_):
    msg_ = re.sub("I don't understand you", '', msg_)
    return re.sub('[ !\n:-]', '', msg_)


def encode(letter_dict, beginning_index, msg='GET-SECRET-DATA'):
    m = ''
    msg = reformat(msg)
    for i, l in enumerate(msg):
        m += letter_dict[l][(i + beginning_index) % 26]
    print(m)


if __name__ == '__main__':
    msg_1 = reformat(msg_1)

    letter_dict = {l: [0]*26 for l in string.ascii_uppercase}

    msg = reformat(msg*30)

    for i, (m_1, m_2) in enumerate(zip(msg, msg_1)):
        letter_dict[m_1][i % 26] = m_2

    for k, val in letter_dict.items():
        print(k, ':', val)

    print(i % 26)

'''
DLM-SDADWK-GCQV
NCU{QQ_M_WYISHJX_PW_KNPEUUDG_SM_GV_PPBHDGKJZ_HZ_VMBQBX_TXRI_VU_GTXZSXTGADB}

A : ['M', 'X', 'P', 'J', 'S', 'T', 'Y', 'Y', 'A', 'T', 'C', 'F', 'V', 'J', 'W', 'U', 'U', 'H', 'M', 'F', 'Y', 'W', 'P', 'P', 'N', 'G']
B : ['H', 'A', 'S', 'L', 'B', 'W', 'S', 'I', 'S', 'V', 'E', 'H', 'G', 'T', 'U', 'D', 'T', 'N', 'Z', 'Y', 'X', 'J', 'B', 'G', 'Y', 'F']
C : ['O', 'E', 'I', 'R', 'F', 'A', 'U', 'K', 'J', 'B', 'A', 'O', 'I', 'N', 'A', 'E', 'V', 'D', 'N', 'C', 'S', 'I', 'G', 'Q', 'C', 'V']
D : ['Q', 'R', 'E', 'U', 'Q', 'O', 'I', 'F', 'X', 'G', 'I', 'N', 'L', 'H', 'R', 'H', 'F', 'U', 'T', 'V', 'V', 'G', 'J', 'V', 'O', 'U']
E : ['L', 'L', 'K', 'Y', 'D', 'E', 'G', 'W', 'D', 'D', 'U', 'P', 'H', 'V', 'Z', 'J', 'H', 'P', 'U', 'A', 'O', 'M', 'Z', 'M', 'B', 'X']
F : ['S', 'V', 'B', 'Z', 'J', 'Z', 'Z', 'C', 'R', 'M', 'Q', 'A', 'Z', 'L', 'K', 'R', 'B', 'Q', 'Q', 'H', 'P', 'T', 'W', 'L', 'D', 'Y']
G : ['D', 'Q', 'T', 'C', 'L', 'F', 'V', 'Z', 'E', 'P', 'W', 'C', 'M', 'M', 'F', 'V', 'M', 'G', 'G', 'Q', 'J', 'E', 'L', 'Y', 'P', 'H']
H : ['I', 'Y', 'N', 'T', 'Z', 'N', 'O', 'P', 'F', 'J', 'N', 'R', 'Q', 'C', 'N', 'M', 'Z', 'O', 'L', 'B', 'G', 'Y', 'S', 'A', 'U', 'S']
I : ['P', 'S', 'U', 'V', 'C', 'D', 'E', 'V', 'Z', 'H', 'V', 'G', 'E', 'O', 'P', 'Y', 'Q', 'T', 'H', 'J', 'K', 'C', 'O', 'H', 'Q', 'W']
J : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
K : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
L : ['Z', 'M', 'O', 'O', 'H', 'L', 'X', 'J', 'P', 'R', 'T', 'T', 'W', 'S', 'Y', 'S', 'X', 'R', 'D', 'G', 'A', 'P', 'A', 'X', 'K', 'N']
M : ['V', 'F', 'D', 'P', 'K', 'Y', 'B', 'B', 'M', 'F', 'P', 'Z', 'Y', 'I', 'M', 'N', 'A', 'K', 'P', 'W', 'E', 'O', 'X', 'W', 'M', 'R']
N : ['Y', 'B', 'Q', 'I', 'N', 'Q', 'W', 'X', 'W', 'I', 'R', 'B', 'T', 'P', 'X', 'P', 'G', 'J', 'E', 'P', 'D', 'Q', 'C', 'E', 'J', 'Z']
O : ['R', 'Z', 'J', 'B', 'O', 'G', 'H', 'G', 'I', 'Q', 'M', 'M', 'U', 'G', 'H', 'Q', 'R', 'B', 'X', 'I', 'H', 'X', 'T', 'Z', 'S', 'P']
P : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Q : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
R : ['X', 'O', 'H', 'F', 'E', 'I', 'D', 'L', 'B', 'K', 'L', 'X', 'K', 'W', 'D', 'I', 'W', 'Y', 'K', 'S', 'F', 'K', 'V', 'O', 'I', 'O']
S : ['G', 'W', 'Y', 'S', 'G', 'J', 'P', 'R', 'Q', 'W', 'O', 'J', 'X', 'R', 'C', 'T', 'J', 'F', 'S', 'U', 'L', 'V', 'H', 'T', 'H', 'E']
T : ['W', 'C', 'M', 'X', 'X', 'B', 'A', 'U', 'K', 'Y', 'S', 'Q', 'C', 'X', 'Q', 'G', 'Y', 'W', 'B', 'K', 'W', 'B', 'Y', 'C', 'Z', 'C']
U : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
V : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
W : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
X : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Y : ['N', 'I', 'V', 'M', 'A', 'U', 'J', 'E', 'V', 'S', 'H', 'I', 'O', 'D', 'V', 'W', 'O', 'X', 'R', 'E', 'T', 'H', 'R', 'D', 'X', 'I']
Z : [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''
loc = 15
stnc = ''
for encripted_letter in 'QQ_M_WYISHJX_PW_KNPEUUDG_SM_GV_PPBHDGKJZ_HZ_VMBQBX_TXRI_VU_GTXZSXTGADB':
    if encripted_letter == '_':
        # print('_')
        stnc += '_'
    else:
        loc +=1
        decripted = '-'
        for k, val in letter_dict.items():
            if val[loc % 26] == encripted_letter:
                decripted = k
        # print(decripted)
        stnc += decripted
print("the flag:")
print(stnc)

'''
CSA{IF_A_MACHINE_IS_EXPECTED_TO_BE_INFALLIBE_IT_CANNOT_ALSO_BE_INTELLIGENT}
'''
