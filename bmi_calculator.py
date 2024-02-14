import numpy as np
height_in=[73,76,65,67,80]
weight_lb=[130,180,180,200,210]

np_height_m=np.array(height_in)* 0.0254
np_weight_kg=np.array(weight_lb) *0.453592

bmi=np_weight_kg/np_height_m**2
print(bmi)

no_of_participants_1=print("Participants number by method 1 : ",len(np.array(np_height_m)))
no_of_participants_2=print("Participants number by method 2 : ",(np.array(np_height_m).size))
no_of_participants_3=print("Participants number by method 3 : ",(np.array(np_height_m).shape))

underweight_participants_no=bmi [bmi<18.5]
print("No of underweight participant(s)",underweight_participants_no.size)
# normal_participants_no=bmi.any()[bmi.any()>=18.5 and bmi.any()<25]                            bujhiyena
# print("No of normal participants: ",normal_participants_no.size)

print(max(bmi))
print(min(bmi))
print(bmi.max())
# print(mean(bmi))
bmi.mean()
print(bmi.mean())

print(bmi[0:3])
print(bmi[-3:-1])



# if bmi.all()>0:
#     print("bmi values: ")
#     if bmi.any()<18.5:
#         print('Underweight')
#     elif bmi.any()>=18.5 and bmi.any()<25:
#         print("Normal")
#     elif bmi.any()>=25 and bmi.any() <30:
#         print("Overweight")
#     else:
#         print("Obesity")
# else:
#     print("Kindly,enter the valid data.")