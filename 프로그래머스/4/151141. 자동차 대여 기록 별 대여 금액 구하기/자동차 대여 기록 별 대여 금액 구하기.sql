SELECT
    HISTORY_ID,
    CASE
        WHEN DATEDIFF(END_DATE,START_DATE)+1 >= 90
            THEN TRUNCATE(DAILY_FEE*(1-0.01*(
                            SELECT DISCOUNT_RATE 
                            FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
                            WHERE DURATION_TYPE = '90일 이상' AND CAR_TYPE = '트럭'
            ))*(DATEDIFF(END_DATE,START_DATE)+1),0)
            
        WHEN DATEDIFF(END_DATE,START_DATE)+1 >= 30
            THEN TRUNCATE(DAILY_FEE*(1-0.01*(
                            SELECT DISCOUNT_RATE 
                            FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
                            WHERE DURATION_TYPE = '30일 이상' AND CAR_TYPE = '트럭'
            ))*(DATEDIFF(END_DATE,START_DATE)+1),0)
            
        WHEN DATEDIFF(END_DATE,START_DATE)+1 >= 7
            THEN TRUNCATE(DAILY_FEE*(1-0.01*(
                            SELECT DISCOUNT_RATE 
                            FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
                            WHERE DURATION_TYPE = '7일 이상' AND CAR_TYPE = '트럭'
            ))*(DATEDIFF(END_DATE,START_DATE)+1),0)
        ELSE TRUNCATE(DAILY_FEE*(DATEDIFF(END_DATE,START_DATE)+1),0)
    END AS FEE
    
FROM CAR_RENTAL_COMPANY_CAR A
JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY B
ON A.CAR_ID = B.CAR_ID
WHERE A.CAR_TYPE = '트럭'
ORDER BY FEE DESC, HISTORY_ID DESC
