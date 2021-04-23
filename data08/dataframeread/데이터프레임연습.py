#!/usr/bin/env python
# coding: utf-8

# In[4]:


print('저의 주피터 서버에 오신 것을 환영합니다.')


# In[3]:


print('2번째 셀 실행')


# # 내가 제목

# ## 나는 누구지?

# In[13]:


### 나는 더 작은 제목


# * 나는 누구지
# * 나는 두번째 목록
# * 나는 세번째 목록

# # 나는 큰 제목
# ## 나는 더 작은 제목
# ### 나는 더더 작은 제목

# * 마크다운
#     * 나는 더 들어갔어

# *나는 기울어졌어*
# 
# **나는 굵어**
# 
# ***나는 굵고 기울어졌어***

# # 제일 큰 제목
# ## 그다음 큰 제목
# ### 아주 작은 제목

# * 아침식사
# * 점심식사
# * 저녁식사
#     * 우동
#     * 라면
# 

# *나는 삐뚤어질거야*
# **나는 찐해질거야**
# ***나는 찐하게 삐뚤어질거야***

# In[16]:


import pandas as pd


# In[28]:


df_2010 = pd.read_csv("../data/2010.csv", encoding='utf-8')
df_2011 = pd.read_csv("../data/2011.csv", encoding='utf-8')
df_2012 = pd.read_csv("../data/2012.csv", encoding='utf-8')


# In[31]:


df_2011


# <img src="../data/9937603E5DD4AF0419.png">

# In[32]:


df_2011


# In[34]:


df_2012


# In[37]:


total_jumsu = pd.concat([df_2010, df_2011, df_2012], ignore_index=True)


# In[38]:


total_jumsu


# In[39]:


total_jumsu['국어']


# In[41]:


total_jumsu['수학']


# In[42]:


total_jumsu.iloc[0]


# In[43]:


total_jumsu.iloc[1]


# In[44]:


total_jumsu.iloc[0:2] #0~1


# In[46]:


total_jumsu.iloc[:,0] #iloc[행, 열], iloc[행]


# In[47]:


df_con1 = pd.read_csv("../data/concat_1.csv", encoding='utf-8')
df_con2 = pd.read_csv("../data/concat_2.csv", encoding='utf-8')
df_con3 = pd.read_csv("../data/concat_3.csv", encoding='utf-8')


# In[52]:


total_jumsu2 = pd.concat([df_con1, df_con2, df_con3], ignore_index=True)


# In[50]:


total_jumsu2


# In[53]:


row_append = df_con1.append(df_con2, ignore_index=True)
row_append


# In[54]:


type(row_append)


# In[55]:


row_append.columns


# In[56]:


inner_result = pd.concat([df_con1, df_con2, df_con3], join='inner')


# In[57]:


inner_result


# In[60]:


inner_result2 = pd.concat([df_con1, df_con3], join='inner')


# In[61]:


inner_result2


# In[62]:
ㄷ
이거이
covid19 = pd.read_csv("../data/country_wise_latest.csv")
covid19


# In[ ]:




ㅎ