import pandas as pd
import numpy as np
import math
import pickle
import streamlit as st


hotel_dict = pickle.load(open('hotel_dict.pkl', 'rb'))
hotel = pd.DataFrame(hotel_dict)
similarity_hotel = pickle.load(open('similarity.pkl', 'rb'))

def recommend(hotel1):
  hotel_index = hotel[hotel['Hotel_Name'] == hotel1].index[0]
  distances = similarity_hotel[hotel_index]
  hotel_list = sorted(list(enumerate(distances)),reverse=True, key= lambda x:x[1])[1:7]
  reconmended_hotel_name=[]
  reconmended_hotel_address = []
  for i in hotel_list:
    reconmended_hotel_name.append(hotel.iloc[i[0]].Hotel_Name)
    reconmended_hotel_address.append(hotel.iloc[i[0]]. Hotel_Address)
  return  reconmended_hotel_name,reconmended_hotel_address

# if st.button('Tìm kiếm'):
#     name = recommend(option_movie_name)
#     for i in name:
#        st.write(i)
#
# st.write(hotel['Nationality'])
# option_movie_name1 = st.selectbox('NHẬP QUỐC TỊCH BẠN MUỐN TÌM',hotel['Nationality'])
# if st.button(' Tìm kiếm'):
#     name = recommend_nati(option_movie_name1)
#     for i in name:
#         st.write(i)


# selected_box = st.sidebar.selectbox('Chọn gợi ý',('Hotel', 'Nationality'))
#
# if selected_box == 'Hotel':
#      hotel()
# if selected_box == 'Nationality':
#      nationality()
def hotel_():
    st.title("Hệ thống gợi ý khách sạn")
    st.subheader('Gợi ý khách sạn bằng tên khách sạn')
    st.write(hotel['Hotel_Name'])
    option_movie_name = st.selectbox('BẠN MUỐN ĐẾN KHÁCH SẠN NÀO?',hotel['Hotel_Name'])
    if st.button('Tìm kiếm'):
        reconmended_hotel_name,reconmended_hotel_address= recommend(option_movie_name)
        st.image('./Anh/1.jpg')
        st.text('Tên khách sạn:')
        st.text(reconmended_hotel_name[0])
        st.text('Địa chỉ khách sạn:')
        st.text(reconmended_hotel_address[0])

        st.image('./Anh/2.jpg')
        st.text('Tên khách sạn:')
        st.text(reconmended_hotel_name[1])
        st.text('Địa chỉ khách sạn:')
        st.text(reconmended_hotel_address[1])

        st.image('./Anh/3.jpg')
        st.text('Tên khách sạn:')
        st.text(reconmended_hotel_name[2])
        st.text('Địa chỉ khách sạn:')
        st.text(reconmended_hotel_address[2])

        st.image('./Anh/4.jpg')
        st.text('Tên khách sạn:')
        st.text(reconmended_hotel_name[3])
        st.text('Địa chỉ khách sạn:')
        st.text(reconmended_hotel_address[3])

        st.image('./Anh/5.jpg')
        st.text('Tên khách sạn:')
        st.text(reconmended_hotel_name[4])
        st.text('Địa chỉ khách sạn:')
        st.text(reconmended_hotel_address[4])

        st.image('./Anh/6.jpg')
        st.text('Tên khách sạn:')
        st.text(reconmended_hotel_name[5])
        st.text('Địa chỉ khách sạn:')
        st.text(reconmended_hotel_address[5])

def welcome():
    st.title('Chào mừng đến với hệ thống gợi ý khách sạn')
    st.image('./anh2.jpg')
def main():
    selected_box = st.selectbox('Chọn gợi ý',('Welcome','Hotel'))
    if selected_box == 'Welcome':
        welcome()
    if selected_box == 'Hotel':
        hotel_()

main()
