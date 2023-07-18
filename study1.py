import streamlit as st

st.title('Streamlit world')
st.header('This is header')
st.subheader('This is subheader')
st.text('This is text')
"hello world with magic"

st.markdown('# This is markdown')
st.markdown('## This is markdown')
st.markdown('''
---
### This is a list
1. First item
2. Second item
3. Third item
---
            
> 하늘을 우르러 한 점 부끄럼이 없기를
> 잎새에 이는 바람에도 나는 괴로워했다.
> 별을 노래하는 마음으로 모든 죽어가는 것을 사랑해야지  

![poster](https://c4.wallpaperflare.com/wallpaper/41/948/967/yorkshire-terrier-dog-backgrounds-puppy-download-3840x2400-yorkshire-terrier-wallpaper-preview.jpg)
                        
''')


st.markdown('''
- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media)
            ''')
st.markdown('---')
st.markdown('[google](https://www.google.com)')


st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('This is write')
st.write(['This is', 'a list'])
st.write({'This': 'is a dictionary'})
st.write({'Name': 'John', 'Age': 25})
st.write('This is a dataframe')

st.audio('./multimedia/music.mp3')
st.video('./multimedia/video.mp4',)
st.image('./multimedia/puppy.jpg')
