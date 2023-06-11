
procedure split (.sep$, .str$)  
  # separate a string into tokens using a delimiter  
  .length = 0  
  repeat    
    .strlen = length(.str$)    
    .sep = index(.str$, .sep$)    
    if .sep > 0      
       .part$ = left$(.str$, .sep-1)      
       .str$ = mid$(.str$, .sep+1, .strlen)    
    else      
       .part$ = .str$    
    endif    
    .length = .length+1    
    .array$[.length] = .part$  
  until .sep = 0 
endproc


dir$ = shellDirectory$ + "/output/utterances/"
wav$ = shellDirectory$ + "/wav"

writeInfo: "Start creating TextGrids for text files in directory: " 
appendInfo: dir$
appendInfoLine: ""

strings = Create Strings as file list: "list_txt", dir$ + "*.txt"
nFiles = Get number of strings

#Create Strings as file list... list_txt 'dir$'/*.txt
#nFiles = Get number of strings


for i from 1 to nFiles
	select Strings list_txt
	filename$ = Get string... i
	basename$ = filename$ - ".txt"
	# appendInfo: "Basename of the text file: "
	# appendInfo: basename$
	# appendInfoLine: ""

    @split: "_", basename$
    wavsubdir$ = split.array$[1]

	txtname$ = filename$ - ".txt"

	Read from file... 'wav$'/'wavsubdir$'/'basename$'.wav
	dur = Get total duration
	To TextGrid... "kaldiphone"
	#pause 'txtname$'

	select Strings list_txt
	Read Table from tab-separated file... 'dir$'/'txtname$'.txt
	Rename... times
	nRows = Get number of rows
	Sort rows... start
	for j from 1 to nRows
		select Table times
		startutt_col$ = Get column label... 5
		# start_col$ = Get column label... 10
		start_col$ = Get column label... 3
		dur_col$ = Get column label... 4
		phone_col$ = Get column label... 7
		
		if j < nRows
			startnextutt = Get value... j+1 'startutt_col$'
		else
			startnextutt = 0
		endif
		start = Get value... j 'start_col$'
		phone$ = Get value... j 'phone_col$'

		@split: "_", phone$
    	phone$ = split.array$[1]

		dur = Get value... j 'dur_col$'
		end = start + dur
		select TextGrid 'basename$'
		int = Get interval at time... 1 start+0.005
		if start > 0 & startnextutt = 0
			Insert boundary... 1 start
			Set interval text... 1 int+1 'phone$'
			Insert boundary... 1 end
		elsif start = 0
			Set interval text... 1 int 'phone$'
		elsif start > 0
			Insert boundary... 1 start
			Set interval text... 1 int+1 'phone$'
		endif
		#pause
	endfor
	#pause
	Write to text file... 'dir$'/'basename$'.TextGrid
	select Table times
	plus Sound 'basename$'
	plus TextGrid 'basename$'
	Remove
endfor