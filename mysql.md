
Exemplo de criação de dados:
Criar um vetor x com n elementos dados por x(i)=cos(i);

Testado no site:
https://onecompiler.com/mysql/42tf4tuwd


```mysql

-- create
CREATE TABLE numeros (
  x DOUBLE
);

-- insert
DELIMITER $$

CREATE PROCEDURE inserir_valores_cos()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE cos_valor DOUBLE;
    WHILE i <= 1 DO
        SET cos_valor = COS(i);  -- Calcula o cos(i)
        INSERT INTO numeros (x) VALUES (cos_valor);  -- Insere o valor na tabela
        SET i = i + 1;  -- Incrementa o contador
    END WHILE;
END$$

DELIMITER ;
CALL inserir_valores_cos();
-- fetch 
SELECT * FROM numeros WHERE 1;
set profiling=1;
SELECT max(x) FROM numeros WHERE 1;
show profiles;

```

```

```