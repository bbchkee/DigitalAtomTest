SELECT 
    station_name AS station_name, 
    SUM(consumption.volume_per_hour*tarif.hour_cost) AS total_cost, 
    SUM(consumption.volume_per_hour*tarif.hour_cost)/COUNT(consumption) AS mean_cost_per_hour 
    FROM station, tarif, consumption 
WHERE 
    tarif.station_id = station.id AND
    consumption.tarif_name = tarif.tarif_name AND
    consumption.hour >= tarif.tarif_begin AND 
    consumption.hour < tarif.tarif_end 
GROUP BY 
    station.id;
