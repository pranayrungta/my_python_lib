set terminal jpeg 

set grid 

set xlabel "btc" 
set ylabel "prob" 

set output "plot_0.jpg" 
set title "plot 0" 
plot "./sample_data//freq_btc_Ring.txt" u 1:3 w lp title "freq btc Ring", 	 \
     "./sample_data//freq_btc_RSF_k=1_ic=100.txt" u 1:3 w lp title "freq btc RSF k=1 ic=100", 	 \
     "./sample_data//freq_btc_RSF_k=2_ic=100.txt" u 1:3 w lp title "freq btc RSF k=2 ic=100", 	 \
     "./sample_data//freq_btc_Star.txt" u 1:3 w lp title "freq btc Star"

set output "RSF_Star.jpg" 
set title "RSF Star" 
plot "./sample_data//freq_btc_RSF_k=1_ic=100.txt" u 1:3 w lp title "freq btc RSF k=1 ic=100", 	 \
     "./sample_data//freq_btc_RSF_k=2_ic=100.txt" u 1:3 w lp title "k=2", 	 \
     "./sample_data//freq_btc_Star.txt" u 1:3 w lp title "Star"


unset output ; exit gnuplot 
