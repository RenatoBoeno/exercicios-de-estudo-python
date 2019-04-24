metros = float (input("digite a quantidade de metros a ser convertida: "))
km = metros /1000
cm = metros *100
mm = metros *1000
dc = metros *10

print ("a media de {}dc {}km {:.0f}m a {}cm e {:.0f}mm".format(dc,km,metros,cm,mm))
