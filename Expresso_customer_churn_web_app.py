import numpy as np
import pickle
import streamlit as st

model = pickle.load(open("Expresso_customer_churn.pkl",'rb' ))


tenure_mapping = {
    'K > 24 month': 7, 
    'I 18-21 month': 5, 
    'G 12-15 month': 3, 
    'H 15-18 month': 4,
    'J 21-24 month': 6, 
    'F 9-12 month': 2, 
    'D 3-6 month': 0, 
    'E 6-9 month': 1
}


top_pack_mapping = {
      'On net 200F=Unlimited _call24H':107, 
      'All-net 500F=2000F;5d':18,
       'On-net 1000F=10MilF;10d':108,
       'Data:1000F=5GB,7d':35,
       'Mixt 250F=Unlimited_call24H':100,
       'MIXT:500F= 2500F on net _2500F off net;2d':96,
        'On-net 500F_FNF;3d':113,
       'Data: 100 F=40MB,24H':30,
       'MIXT: 200mnoff net _unl on net _5Go;30d':88,
       'Jokko_Daily':84,
       'Data: 200 F=100MB,24H':31, 
        'Data:490F=1GB,7d':44,
       'Twter_U2opia_Daily':123, 
       'On-net 500=4000,10d':112, 
       'Data:1000F=2GB,30d':34,
       'IVR Echat_Daily_50F':77, 
       'Pilot_Youth4_490':116,
       'All-net 500F =2000F_AllNet_Unlimited':16, 
        'Twter_U2opia_Weekly':125,
       'Data:200F=Unlimited,24H':40, 
        'On-net 200F=60mn;1d':110,
       'All-net 600F= 3000F ;5d':20, 
        'Pilot_Youth1_290':115,
       'All-net 1000F=(3000F On+3000F Off);5d':12, 
        'VAS(IVR_Radio_Daily)':126,
       'Data:3000F=10GB,30d':41, 
        'All-net 1000=5000;5d':11,
       'Twter_U2opia_Monthly':124, 
       'MIXT: 390F=04HOn-net_400SMS_400 Mo;4h\t':89,
       'FNF2 ( JAPPANTE)':69, 
       'Yewouleen_PKG':134, 
       'Data:150F=SPPackage1,24H':39,
       'WIFI_Family_2MBPS':131, 
        'Data:500F=2GB,24H':45,
        'MROMO_TIMWES_RENEW':98,
       'New_YAKALMA_4_ALL':105,
        'Data:1500F=3GB,30D':37,
       'All-net 500F=4000F ; 5d':19,
        'Jokko_promo':87,
        'All-net 300=600;2d':13,
       'Data:300F=100MB,2d':42,
      'MIXT: 590F=02H_On-net_200SMS_200 Mo;24h\t\t':93,
       'All-net 500F=1250F_AllNet_1250_Onnet;48h':17, 
        'Facebook_MIX_2D':71,
       '500=Unlimited3Day':8,
       'On net 200F= 3000F_10Mo ;24H':106, 
       '200=Unlimited1Day':3,
        'YMGX 100=1 hour FNF, 24H/1 month':132,
       'SUPERMAGIK_5000':120,
        'Data:DailyCycle_Pilot_1.5GB':49,
        'Staff_CPE_Rent':121,
       'MIXT:1000F=4250 Off net _ 4250F On net _100Mo; 5d':95,
       'Data:50F=30MB_24H':46,
        'Data:700F=SPPackage1,7d': 48,
       'Data: 490F=Night,00H-08H':33, 
        'Data:700F=1.5GB,7d': 47,
       'Data:1500F=SPPackage1,30d': 38, 
        'Data:30Go_V 30_Days': 43,
       'MROMO_TIMWES_OneDAY':  97, 
        'On-net 300F=1800F;3d': 111, 
       'All-net 5000= 20000off+20000on;30d': 14,
        'WIFI_ Family _4MBPS': 130,
       'CVM_on-net bundle 500=5000':  29, 
        'Internat: 1000F_Zone_3;24h\t\t':  82,  
       'DataPack_Incoming':52,
        'Jokko_Monthly':85,
        'EVC_500=2000F':  61, 
       'On-net 2000f_One_Month_100H; 30d':109,
       'MIXT:10000F=10hAllnet_3Go_1h_Zone3;30d\t\t': 94, 
        'EVC_Jokko_Weekly': 64,
       '200F=10mnOnNetValid1H': 5,
        'IVR Echat_Weekly_200F': 79,
       'WIFI_ Family _10MBPS':129, 
        'Internat: 1000F_Zone_1;24H\t\t': 81,
       'Jokko_Weekly':  86,
        'SUPERMAGIK_1000': 119,
       'MIXT: 500F=75(SMS, ONNET, Mo)_1000FAllNet;24h\t\t':  92, 
       'VAS(IVR_Radio_Monthly)':127,
       'MIXT: 5000F=80Konnet_20Koffnet_250Mo;30d\t\t':91,
       'Data: 200F=1GB,24H':  32,  
        'EVC_JOKKO30': 63,
       'NEW_CLIR_TEMPALLOWED_LIBERTE_MOBILE': 103, 
        'TelmunCRBT_daily': 122,
       'FIFA_TS_weekly':  68, 
        'VAS(IVR_Radio_Weekly)': 128,
       'Internat: 2000F_Zone_2;24H\t\t':  83, 
        'APANews_weekly':  10,
        'EVC_100Mo':  58,
       'pack_chinguitel_24h': 135,
        'Data_EVC_2Go24H':  53,
       'Mixt : 500F=2500Fonnet_2500Foffnet ;5d': 101, 
        'FIFA_TS_daily':66,
       'MIXT: 4900F= 10H on net_1,5Go ;30d':  90,
        'CVM_200f=400MB':  25,
       'IVR Echat_Monthly_500F':  78, 
        'All-net 500= 4000off+4000on;24H':  15,
       'FNF_Youth_ESN': 70, 
        'Data:1000F=700MB,7d':  36, 
        '1000=Unlimited7Day':   0,
       'Incoming_Bonus_woma':  80, 
        'CVM_100f=200 MB':  22, 
        'CVM_100F_unlimited':  21,
       'pilot_offer6': 138,   
        '305155009':7, 
        'Postpaid FORFAIT 10H Package':117,  
       'EVC_1Go':59,
        'GPRS_3000Equal10GPORTAL':72,
       'NEW_CLIR_PERMANENT_LIBERTE_MOBILE':102, 
        'Data_Mifi_10Go_Monthly':55,
       '1500=Unlimited7Day':1, 
        'EVC_700Mo':62, 
        'CVM_100f=500 onNet':23,
       'CVM_On-net 1300f=12500':27, 
        'pilot_offer5':137, 
        'EVC_4900=12000F':60,
       'CVM_On-net 400f=2200F':28, 
        'YMGX on-net 100=700F, 24H':133,
       'CVM_150F_unlimited':24,
        'EVC_MEGA10000F':65, 
        'pilot_offer7':139,
       'CVM_500f=2GB':26, 
        'SMS Max':118, 
        '301765007':6, 
        '150=unlimited pilot auto':2,
       'MegaChrono_3000F=12500F TOUS RESEAUX':99,
        'pilot_offer4':136,
       'Go-NetPro-4 Go':76, 
        '200=unlimited pilot auto':4,
       'ESN_POSTPAID_CLASSIC_RENT':57, 
        'Data_Mifi_10Go':54,
       'Data:New-GPRS_PKG_1500F':50, 
        'GPRS_BKG_1000F MIFI':74,
       'Data:OneTime_Pilot_1.5GB':51, 
        'FIFA_TS_monthly':67,
       'GPRS_PKG_5GO_ILLIMITE':75,
        'Data_Mifi_20Go': 56,
        'APANews_monthly':9,
       'NEW_CLIR_TEMPRESTRICTED_LIBERTE_MOBILE':104, 
        'GPRS_5Go_7D_PORTAL':73,
       'Package3_Monthly:114':114
         }

def customers_prediction(user_input):
    #convert data into an array
    input_array = np.asarray(user_input)

    
    #reshaped data into a two dimensional array
    reshaped_array = input_array.reshape(1, -1)

    #getting predicction
    prediction =model.predict(reshaped_array)
    if prediction == 0:
        return "This customer will stay!"
    else:
        return "This customer will go"
    
        
def main():
    st.title("Expresso Customer Churn Prediction Web App")

    Tenure = st.selectbox("customer's tenure:", list(tenure_mapping.keys()))
    encoded_tenure =tenure_mapping[Tenure]
    Montant = st.text_input("Top-up Amount of the customer")
    Frequence_rech = st.text_input("Number of times the customer refilled")
    Revenue= st.text_input("monthly income of each customer	")
    On_net= st.text_input("Amount spent on each Expresso call")
    Orange = st.text_input("Amount spent on call to orange")
    Regurality = st.text_input("number of times the customer is active for 90 days")
    Top_pack = st.selectbox("Top package on expresso network:", list(top_pack_mapping.keys()))
    encoded_top_pack = top_pack_mapping[Top_pack]
    Freq_top_pack = st.text_input("number of times the client has activated the top pack packages")
    

    performance = ""

    if st.button("Eligibility Result"):
        performance = customers_prediction([(encoded_tenure), float(Montant), float(Frequence_rech), float(Revenue), float(On_net), float(Orange), float(Regurality), (encoded_top_pack), float(Freq_top_pack)])
        st.success(performance)

        
if  __name__ == "__main__":
    main()
