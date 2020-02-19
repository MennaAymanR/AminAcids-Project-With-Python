print("\t Menna Ayman Rashad \t")
print("\t Hello in Amino acid program \t")
print("*************************************************************")


aminoname=input("Enter the name of amino acid:")
aminoname=aminoname.upper()
aminoacids=["TTT","TTC","TTA","TTG","TCT","TCC","TCA","TCG","TAT","TAC","TAA"
,"TAG","TGT","TGC","TGA","TGG","CTT","CTC","CTA","CTG","CCT","CCC","CCA","CCG","CAT"
,"CAC","CAA","CAG","CGT","CGC","CGA","CGG","ATT","ATC","ATA","ATG","ACT","ACC","ACA"
,"ACG","AAT","AAC","AAA","AAG","AGT","AGC","AGA","AGG","GTT","GTC","GTA","GTG","GCT"
,"GCC","GCA","GCG","GAT","GAC","GGT","GGC","GGA","GGG"]
aminoacidsname=["Phe(F)","Phe(F)","Leu(L)","Leu(L)","Ser(S)","Ser(S)","Ser(S)","Ser(S)"
,"Tyr(Y)","Tyr(Y)","Stop","Stop","Cys(C)","Cys(C)", "Stop", "Trp(W)" ,"leu(L)","leu(L)"
,"leu(L)","leu(L)","Pro(P)","Pro(P)","Pro(P)","Pro(P)","His(H),His(H)","Gln(G)","Gln(G)"
,"Arg(R)","Arg(R)","Arg(R)","Arg(R)","Ile(I)","Ile(I)","Ile(I)","Met(M)","Thr(T)","Thr(T)"
,"Thr(T)","Thr(T)","Asn(N)","Asn(N)","Lys(K)","Lsy(K)","Ser(S)","Ser(S)","Ser(S)","Arg(R)"
,"Arg(R)","Val(v)","Val(v)","Val(v)","Val(v)","Asp(D)","Asp(D)","Glu(E)","Glu(E)","Gly(G)"
,"Gly(G)","Gly(G)","Gly(G)"]
i=0
find=False
for X in aminoacids:
    if(X==aminoname):
        print("The amino acid you entered is:"+ aminoacidsname[i])    
        find=True
    i+=1        
if (find==False):
    print("Wrong Amino acid")    
    

 


        