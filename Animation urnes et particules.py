#Animation
import numpy as np
import matplotlib.pyplot as plt
N=1000
T=5000
#plt.clf()
bord=[[1,1],[0,1]]
X=np.random.rand(2,N)
#col=np.random.rand(N,3)
#X=np.array([np.random.uniform(0,2,N),np.random.rand(N)])
fig,ax=plt.subplots(1,1,figsize=(9,8))
ax.plot(bord[0],bord[1])
ax.scatter(X[0,:],X[1,:],s=2,c='r',marker='*')
plt.xlim([0,2])
plt.ylim([0,1])
#ite=0
for i in range(T):
    u=np.random.randint(0,N,1)[0]
    #print(u)
    if X[0,u]<1:
        X[0,u]=X[0,u]+1
    else:
        X[0,u]=X[0,u]-1
    if i%50==0:
        plt.cla()
        total=len(np.where(X[0,:]<=1)[0])
        plt.title(' {}  vs {} particules'.format(total,N-total))
        ax.plot(bord[0],bord[1])
        ax.scatter(X[0,:],X[1,:],s=2,c='r',marker='*')
        plt.xlim([0,2])
        plt.ylim([0,1])
        plt.draw()
        plt.pause(.2)
        plt.show()
       # plt.savefig('urn1/anim'+str(ite)+'.png',dpi=300)
        #ite+=1

