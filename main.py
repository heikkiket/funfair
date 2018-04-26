import parser

hello = "ask bumper car operator to a cafeteria"
parser.process_sentence(hello)

def direct_to_name (loc):
    location={"n":"North","e":"East","s":"South","w":"West","ne":"Northeast","se":"Southeast","sw":"Southwest","nw":"Northwest"}
    return location[loc]

x=direct_to_name("ne")
print ("Hello "+x)
