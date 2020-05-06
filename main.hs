-- IMPORT Data.List
-- import System.IO

-- Int -2^63 2^63
cardinality_S = 5 :: Int
s_set = [1..5]
r1 :: Double
r1 = 2 :: Double
r2 = 1 :: Double
delta = 20 :: Double
c1 = 10 :: Double
c2 = 5 :: Double
c3 = 7 :: Double
n_set = [1,2,3,4]
g = [8000,8000,8000,8000]
-- x_tilde_data = [1.0,1.0,1.0,1.0,1.0]
-- tilde_d_data = [0.0,600.0..1800.0]
-- tilde_w_data = [[0.0,12.0,12.0,12.0,12.0],
           -- [0.0,0.0,12.0,12.0,12.0],
           -- [0.0,0.0,0.0,12.0,12.0],
           -- [0.0,0.0,0.0,0.0,12.0],
           -- [0.0,0.0,0.0,0.0,0.0]]
-- lambda_data = [[0.0,0.05,0.05,0.05,0.05],
          --[0.0,0.0,0.05,0.05,0.05],
          --[0.0,0.0,0.0,0.05,0.05],
          --[0.0,0.0,0.0,0.0,0.05],
          --[0.0,0.0,0.0,0.0,0.0]]
-- t_data = [[60,60,60,60],
     --[60,60,60,60],
     --[60,60,60,60],
     --[60,60,60,60]]
-- o_data = [[0.0,1.0,1.0,1.0,1.0],
     --[0.0,0.0,1.0,1.0,1.0],
     --[0.0,0.0,0.0,1.0,1.0],
     --[0.0,0.0,0.0,0.0,1.0],
     --[0.0,0.0,0.0,0.0,0.0]]

tilde_d(n) = 600.0*(fromIntegral(n-1))
o(s,y)
   | y>s = 1.0
   | y<=s = 0.0
x_tilde(s) = 1.0
tilde_w(s,y)
   | y>s = 12.0
   | y<=s = 0.0
lambda(s,y)
   | y>s = 0.0166
   | y<=s = 0.0
t(n,s) = 60.0


l(n,s,y)
   | y<=s = 0
   | y>s = o(s,y)*(w(n,s,y)-(w(n,s,y)*x(n,s)*x(n,y)))

m :: (Int,Int) -> Double
m(n,s) = sum(addlist)
   where addlist = [o(s,y)*l(n,s,y) | y<-s_set, y>=s+1]

w :: (Int,Int,Int) -> Double
w(n,s,y)
   | n==1 = tilde_w(s,y)
   | n>1 && y < s+1 = 0
   | n>1 && y >= s+1 = l(n-1,s,y)+lambda(s,y)*h(n,s)

u :: (Int,Int) -> Double
u(n,s)
   | s == cardinality_S = 0
   | s < cardinality_S = sum(addlist)
   where addlist = [x(n,s)*w(n,s,y)*x(n,y)*o(s,y) | y <- s_set, y>=s+1]

b :: (Int,Int,Int) -> Double
b(n,s,y)
   | y>=s+1 = x(n,s)*w(n,s,y)*x(n,y)
   | y<=s = 0

v :: (Int,Int) -> Double
v(n,s)
   | s==1 = 0
   | s/=1 = sum(addlist)
   where addlist = [x(n,s)*(w(n,y,s) :: Double)*(x(n,y) :: Double) | y<-s_set, y<=s-1]

k :: (Int,Int) -> Double
k(n,s) = r1*u(n,s)+r2*v(n,s)
gamma(n,s)
   | s==1 = u(n,s)
   | s/=1 = gamma(n,s-1)+u(n,s)-v(n,s)

a :: (Int,Int) -> Double
a(n,s)
   | s==2 = tilde_d(n) + t(n,1) + (0.5 :: Double)
   *((delta::Double)*((x(n,1)::Double)+(x(n,2)::Double)))
   | s>=3 = d(n,s-1)+t(n,s-1)+0.5*(delta*(x(n,s-1)+x(n,s)))

d :: (Int,Int) -> Double
d(n,s)
   | s>1 = a(n,s)+k(n,s)
   | s==1 = tilde_d(n)

h :: (Int,Int) -> Double
h(n,s)
   | s>1 = a(n,s)-d(n-1,s)
   | s==1 = tilde_d(n) - tilde_d(n-1)

x :: (Int,Int) -> Double
x(n,s) = 1
--(if n==4 && s/=1 && s/=5 then 0 else 1)



objectivefunction = c1*sum(sumList1)+c2*sum(sumList2)+c3*sum(sumList3)
   where sumList1 = [(u(n,s)-m(n-1,s))*0.5*h(n,s) + m(n-1,s)*(0.5*h(n-1,s)+k(n-1,s)+h(n,s)) | n<-n_set,n>=3, s<-s_set, s/=cardinality_S]
         sumList2 = [b(n,s,y)*( t(n,z-1)+(k(n,z)+delta)*x(n,z)) | n<-n_set,n>=2,s<-s_set,s<cardinality_S,y<-s_set,y>=s+1,z<-s_set,z>=s+1,z<=y]
         sumList3 = [t(n,s-1)+(k(n,s)+delta)*x(n,s) | n<-n_set,n>=2,s<-s_set,s>=2]

cartProd xs ys = [(x,y) | x <- xs, y <- ys]
-- all_set=[1..50000]

-- all_scores = [objectivefunction(i) | i <-all_set]










