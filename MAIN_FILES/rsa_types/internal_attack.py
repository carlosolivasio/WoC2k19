#used to find private key of a company's head, when his N and e is public...
#you work in said company and have your own key (e,d)

import binascii

def ext_Euclid(a,b):
  if a>b:   #reversing values of a and b
    a=a+b
    b=a-2*b
    a=(a-b)//2
    b=a+b

  c=a   #calling vals of a and c for calcing
  d=b

  uc=1  #these vars are used for maintaining the 'if' condition
  vc=0
  ud=0
  vd=1

  while c!=0:
    if uc*a+vc*b==c and ud*a+vd*b==d:  #main invariant condition
        q=d//c
        m=c  #storing c
        c=d-q*c
        d=m
        
        Uc=uc #storing uc and vc
        Vc=vc
        
        uc=ud-q*uc
        vc=vd-q*vc
        ud=Uc
        vd=Vc

  if ud<0:
      ud=ud+b
  
  return ud

def company(n,e_CEO,c):

  e=65537
  d=205119704640110252892051812353

  k=round(((e*d)-1)/n)#checking approximations since phi is pretty close to n

  while True:
    phi=((e*d)-1)//k
    if phi*k==((e*d)-1):
      print("totient:",phi)
      break
    else:
      k+=1

  d_CEO=ext_Euclid(e_CEO,phi)

  print("d-CEO:",d_CEO)


  m=pow(c,d_CEO,n)

  message=binascii.unhexlify(hex(m)[2:]).decode()

  return message
