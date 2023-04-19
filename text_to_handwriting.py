import pywhatkit as pw
text="""The mechanical engineering field requires an understanding of core areas including mechanics, dynamics, thermodynamics""",""" materials science, structural analysis, and electricity. In addition to these core principles, mechanical engineers use tools such as computer-aided design (CAD), computer-aided manufacturing (CAM), and product lifecycle management to design and analyze manufacturing plants, industrial equipment and machinery, heating and cooling systems, transport systems, aircraft, watercraft, robotics, medical devices, weapons, and others. It is the branch of engineering that involves the design, production, and operation of machinery.[2][3]
"""
pw.text_to_handwriting(text,"demo1.png",[0,0,1])#text , file-name , color( jo file na e ma kai parameter na apie to default ma pywhatkit.png save thai and color blue save thai)
print("end")

# aa program mate net ni jarur pade 