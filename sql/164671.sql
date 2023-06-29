-- 코드를 입력하세요
SELECT CONCAT('/home/grep/src/',B.BOARD_ID,'/',B.FILE_ID,B.FILE_NAME,B.FILE_EXT) AS FILE_PATH
FROM USED_GOODS_BOARD A JOIN USED_GOODS_FILE B ON A.BOARD_ID = B.BOARD_ID
WHERE A.VIEWS IN (SELECT MAX(VIEWS)
                FROM USED_GOODS_BOARD)
ORDER BY B.FILE_ID DESC