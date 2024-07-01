import streamlit as st
from datetime import datetime

st.title('Hello World')
# Title
st.title('Title - GFG')

# Header
st.subheader('Title - GFG')

# Text
st.text('Text -GFG')

# Markdown
st.markdown('This is a list of h tags using markdown.') #p
st.markdown('# GFG') #h1
st.markdown('## GFG') #h2
st.markdown('### GFG') #h3
st.markdown('#### GFG') #h4
st.markdown('##### GFG') #h5
st.markdown('###### GFG') #h6

st.markdown('**GFG** is an Ed tech')  #Bold
st.markdown('__GFG__ is an Ed tech')  #Bold

st.markdown('*GFG* is an Ed tech')  # Italic
st.markdown('_GFG_ is an Ed tech')  # Italic

st.markdown('***GFG*** is an Ed tech')  # Bold + Italic
st.markdown('___GFG___ is an Ed tech')  # Bold + Italic

st.markdown('- First Point')
st.markdown('- Second Point')

st.write('Text')
st.write(range(1,10))
st.text(range(1,10))

#------------------------------------------------------------
st.subheader('1. Text Input')
name =st.text_input('Enter your name: ',value ='Anurag Kumar')  #text input,taking bydefault Anurag Kumar as input
st.write('Hello !',name)

st.subheader('2.Enter the Password.')
password =st.text_input('Enter your password : ',type ='password',help ='Atleast have 8 character.')

st.subheader('3. Text Area')
st.text_area('Tell me about yourself: ',value ='Anurag' ,height =200 ,max_chars =500,
   help ='Max 500 chars are allowed.')

st.subheader('4. Numeric Input')
st.number_input('Enter your age : ',min_value =0,max_value =110,step =1,value =26)

st.header('5. Numeric Input')
today =datetime.now().date()

date =st.date_input('Enter the date : ',value =today ,min_value =today ,max_value =today.replace(year = today.year +1))
st.write('You have selected : ',datetime.strftime(date ,'%d/%m/%Y'))

st.subheader('6.Radio Button')
gender =st.radio('Select your gender : ',options =('Male','Female','Others'), help='Choose One' ,horizontal =True)
st.write("You've selected", gender)

st.subheader('7. Select Box')
option =st.selectbox('Select your options : ', options =('Data Analysis','Machine learning','Deep Learning','AI') ,help='Choose One' )
st.write("You've selected", option)

st.subheader('8. MultiSelect Box')
options =st.multiselect('Select your options : ',options =('DA','ML','DL','AI'),default ='DL')

st.subheader('9. Button')
if st.button('Say Hello'):
    st.write('Hi',name)

st.subheader('10. Checkbox')
if st.checkbox('I agrre to terms and conditions.' ,help ='Agreed to Procced'):
    st.write('Thanks for this.')

st.subheader('Color Picker')
color_selected =st.color_picker('Select you color:' ,'#0F1390')
st.write("You have selected",color_selected)

st.button('Submit your response.')

st.title('BMI Calculator.')

with st.form('BMI Calculator.'):
    col1, col2, col3 =st.columns([3,2,1])
with col1:
    weight =st.number_input('Enter your weight in KGs')
with col2:
    height =st.number_input('Enter your height in meter')
with col3:
    submit =st.form_submit_button('Calculate.')

if submit:
    BMI =round((weight / (height**2)),2)
    if(BMI <=18.5):
        st.error('UnderWeight')

    elif(BMI >18.5 and BMI <=24.5):
        st.success('Healthy')
    elif(BMI >=25 and BMI <=29.9):
        st.warning('Overweight')
    elif(BMI >=30.0):
        st.error('Obese')
