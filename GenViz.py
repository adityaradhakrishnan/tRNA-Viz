# This script requires the Requests Python library which can be installed through 'pip'.
#
# Edit the URL to the organism of interest!

URL = 'http://gtrnadb.ucsc.edu/genomes/bacteria/Esch_coli_K_12_MG1655/Esch_coli_K_12_MG1655-gene-list.html'
# URL = 'http://gtrnadb.ucsc.edu/genomes/eukaryota/Scere3/Scere3-gene-list.html'
# URL = 'http://gtrnadb.ucsc.edu/genomes/eukaryota/Hsapi19/Hsapi19-gene-list.html'

def drawPoint(Pos,Val,Col,File,Case):

	if Case[0] == 1:
		File.write(' '.join(map(str, Pos[0:2])) + ' 14 0 360 arc closepath\n')
		File.write(' '.join(map(str, [i*.5 for i in Col])) + ' setrgbcolor fill\n')

		File.write(' '.join(map(str, Pos[0:2])) + ' 12 0 360 arc closepath\n')
		File.write(' '.join(map(str, [i*.75 for i in Col])) + ' setrgbcolor fill\n')

		File.write(' '.join(map(str, Col)) + ' setrgbcolor fill\n')
		File.write('/Helvetica findfont\n14 scalefont setfont newpath\n')

		if len(Val) == 1:
			File.write(str(Pos[0] - 3.5) + ' ' +  str(Pos[1] - 5) + ' moveto (' + str(Val) + ') show\n')
		else:
			File.write(str(Pos[0] - 8) + ' ' +  str(Pos[1] - 5) + ' moveto (' + str(Val) + ') show\n')

	if Case[0] == 0:
		File.write(' '.join(map(str, Pos[0:2])) + ' 7 0 360 arc closepath\n')
		File.write(' '.join(map(str, [i*.5 for i in Col])) + ' setrgbcolor fill\n')

		File.write(' '.join(map(str, Pos[0:2])) + ' moveto ')
		File.write(str(Pos[0]) + ' ' + str(Pos[1] + Case[1]*19) + ' lineto 2 setlinewidth stroke closepath\n')

		File.write(' '.join(map(str, Pos[0:2])) + ' 5 0 360 arc closepath\n')
		File.write(' '.join(map(str, [i*.75 for i in Col])) + ' setrgbcolor fill\n')

	if Pos[2]%4 == 0:
		if Pos[2]%16 == 0:
			Pos = [Pos[0] - 390, Pos[1] - 20, Pos[2]]
		else:
			Pos = [Pos[0] + 130, Pos[1] + 124, Pos[2]]

	return [Pos[0], Pos[1] - 31, Pos[2]]

def finishTable(File,Pos,Colors):
	InitPos = Pos
	Pos     = [Pos[0] - 30, Pos[1] - 8, 0]

	for IdxC in Colors.keys():
		Col = Colors[IdxC]
	
		File.write(' '.join(map(str, Pos[0:2])) + ' 14 0 360 arc closepath\n')
		File.write(' '.join(map(str, [i*.5 for i in Col])) + ' setrgbcolor fill\n')
		File.write(' '.join(map(str, Pos[0:2])) + ' 12 0 360 arc closepath\n')

		File.write(' '.join(map(str, [i*.75 for i in Col])) + ' setrgbcolor fill\n')
		
		File.write('0 0 0 setrgbcolor fill\n')
		File.write('/Helvetica findfont\n14 scalefont setfont newpath\n')
		if IdxC != '':
			File.write(str(Pos[0] + 20) + ' ' +  str(Pos[1] - 5) + ' moveto (' + str(IdxC) + ') show\n')
		else:
			File.write(str(Pos[0] + 20) + ' ' +  str(Pos[1] - 5) + ' moveto (Unmodified) show\n')

		Pos = [Pos[0] + 140, Pos[1], Pos[2] + 1]

		if Pos[2]%4 == 0:
			Pos = [Pos[0] - 560, Pos[1] - 31, Pos[2]]

	Pos = [InitPos[0] - 50, InitPos[1] + 92, 0]
	Nucleotides = ['G','A','T','C']

	for IdxN in range(0,4):
		File.write('0 0 0 setrgbcolor fill\n')
		File.write('/Helvetica-Bold findfont\n28 scalefont setfont newpath\n')
		File.write(str(Pos[0]) + ' ' +  str(Pos[1]) + ' moveto (' + Nucleotides[-(IdxN + 1)] + ') show\n')

		Pos = [Pos[0], Pos[1] + 142, 0]

	Pos = [Pos[0] + 38, Pos[1] - 58, 0]

	for IdxN in range(0,4):
		File.write('0 0 0 setrgbcolor fill\n')
		File.write('/Helvetica-Bold findfont\n28 scalefont setfont newpath\n')
		File.write(str(Pos[0]) + ' ' +  str(Pos[1]) + ' moveto (' + Nucleotides[IdxN] + ') show\n')

		Pos = [Pos[0] + 131, Pos[1], 0]

	Pos = [Pos[0] - 90, Pos[1] - 32, 0]

	File.write('0 0 0 setrgbcolor fill\n')
	File.write('/Helvetica-Bold findfont\n18 scalefont setfont newpath\n')
	File.write(str(Pos[0]) + ' ' +  str(Pos[1]) + ' moveto (G) show\n')

	for Idx in range(0,4):
		for IdxN in range(0,4):
			File.write('0 0 0 setrgbcolor fill\n')
			File.write('/Helvetica-Bold findfont\n18 scalefont setfont newpath\n')
			File.write(str(Pos[0]) + ' ' +  str(Pos[1]) + ' moveto (' + Nucleotides[IdxN] + ') show\n')

			Pos = [Pos[0], Pos[1] - 31, 0]
		Pos = [Pos[0], Pos[1] - 20, 0]

def assignColors(Modifications):
	
	Colors  = {0:[1,0.988,0.098], 1:[1, 0.776, 0.0745], 2:[0.078,0.622,1], 3:[0.235,0.943,0.2698],
		      4:[0.751,0.318,0.898], 5:[1,0.514,0.198], 6:[0.078,0.8,0.557], 7:[0.504,0.420,0.798],
		      8:[0.061,0.721,0.193], 9:[0.117,0.8,0.254], 10:[0.892,0.543,0.622], 11:[0.666,0.666,0.666],
		      12:[0.998,0.201,0.201]}

	ModDict = {'Stop': Colors[12]}

	for Idx in range(len(Modifications)):
		ModDict[Modifications[Idx]] = Colors[Idx]

	return ModDict

import requests, json, os, itertools
from string import maketrans 

TransDict = maketrans('ACGT','TGCA')
Nucleotides = ['G','A','T','C']

Response = requests.get(URL)

Start    = Response.text.find('ajax') + 8
Stop     = Response.text.find('pageLength') - 8
String   = Response.text[Start:Stop]

if not os.path.exists(String):
	Base     = '/'.join(URL.split('/')[0:6]) + '/'
	URL      = Base + String
	
	FileOut  = open(String,'w')
	FileOut.write(requests.get(URL).text)
	FileOut.close()

with open(String) as DataFile:
	Data = json.load(DataFile)
	DataFile.close()

if 'modifications' not in Data['data'][0].keys():
	for Idx in range(0, len(Data['data'])):
		tRNAID   = str(Data['data'][Idx]['GtRNAdbID'])
		Response = requests.get(Base + '/genes/' + tRNAID + '.html')

		Start    = Response.text.find('Known Modifications') + 120
		Text     = Response.text[Start:(Start + 200)]
		Stop     = Text.find('</td>')
		Data['data'][Idx]['modifications'] = Text[0:Stop]

	with open(String,'w') as DataFile:
		json.dump(Data, DataFile)
		DataFile.close()

tRNADict  = {}
ModList   = ['']

for Idx in range(0,len(Data['data'])):

	Split  = Data['data'][Idx]['GtRNAdbID'].split('-')
	Acodon = str(Split[2])[::-1].translate(TransDict)
	Start  = Data['data'][Idx]['modifications'].find('34')
	Mod    = str(Data['data'][Idx]['modifications'])[(Start - 10):(Start + 1)].split(' ')[-1][:-1]

	tRNADict[Acodon] = [tRNADict[Acodon][0] + 1, tRNADict[Acodon][1] + ''] if Acodon in tRNADict else [1, Mod]

	if (Mod not in ModList):
		ModList.append(Mod) 

Colors = assignColors(ModList)	

FileOut = open('tRNA-Table.ps','w')
FileOut.write("%!PS-Adobe-2.0\n")

Position = [100, 715, 0] # x-Position, y-Position, Counter

for Idx in itertools.product(Nucleotides, Nucleotides, Nucleotides):
	Position[2] += 1
	Codon        = ''.join(Idx)

	if Codon in tRNADict:
		Position = drawPoint(Position, str(tRNADict[Codon][0]), Colors[tRNADict[Codon][1]], FileOut, [1,0])
	elif Codon in ['TGA','TAA','TAG']:
		Position = drawPoint(Position, 'x', Colors['Stop'], FileOut, [1,0])
	else:
		ShiftDict = {'G':'A','A':'G','T':'C','C':'T'}
		Codon     = Codon[0:2] + ShiftDict[Codon[2]]
		if Codon[2] in ['G','T']:
			Position = drawPoint(Position, str(tRNADict[Codon][0]), Colors[tRNADict[Codon][1]], FileOut, [0,1])
		else:
			Position = drawPoint(Position, str(tRNADict[Codon][0]), Colors[tRNADict[Codon][1]], FileOut, [0,-1])

finishTable(FileOut,Position,Colors)
