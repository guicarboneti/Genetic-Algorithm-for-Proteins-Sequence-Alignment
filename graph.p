set term png
set output "grafico1.png"
plot "result.csv" using 1:2 with lines lt 2 title "Generation vs Fitness", \
"result.csv" using 1:3 with lines lt 3 title "Average Fitness"