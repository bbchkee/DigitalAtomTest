SELECT 
    station_name AS station_name, 
    SUM(tarif.hour_cost)/COUNT(tarif) AS mean_cost_per_hour,
    SUM(consumption.volume_per_hour*tarif.hour_cost) AS total_cost            
FROM        
    station INNER JOIN tarif 
        ON tarif.station_id = station.id
    LEFT OUTER JOIN consumption
        ON consumption.tarif_name = tarif.tarif_name AND
           consumption.hour >= tarif.tarif_begin AND 
           consumption.hour < tarif.tarif_end
WHERE 
    tarif.station_id = station.id
GROUP BY 
    station.id
ORDER BY 
    station.id
