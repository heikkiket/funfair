import parser


#Dmitri
def direct_to_name (loc):
    location={"n":"North","e":"East","s":"South","w":"West","ne":"Northeast","se":"Southeast","sw":"Southwest","nw":"Northwest"}
    return location[loc]

x=direct_to_name("ne")
print ("Hello "+x)
