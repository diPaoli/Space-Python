import MySQLdb

host='localhost'
db='SpacePython'
user='SpacePython'
pw='123456'
port = 3306

#conn = MySQLdb.Connection()
#c = conn.cursor()


def connect_DB():
    return MySQLdb.Connection(host, user, pw, db)


def select(name):
    query = "SELECT * FROM tb_scores WHERE pl_name = %s"

    conn = connect_DB()
    c = conn.cursor()
    c.execute(query,[name])
    conn.close()
    return c.fetchall()



def select_all():
    query = "SELECT * FROM tb_scores ORDER BY high_score DESC"

    conn = connect_DB()
    c = conn.cursor()
    c.execute(query)
    conn.close()
    return c.fetchall()



def insert(name, last_score, high_score):
    
    query = "INSERT INTO tb_scores VALUES(%s, %s, %s)"
    val = (name, last_score, high_score)

    conn = connect_DB()
    c = conn.cursor()
    c.execute(query, val)
    conn.commit()
    conn.close()



def update_Score(name, score):
    
    query = "UPDATE tb_scores SET last_score = %s WHERE pl_name = %s"
    val = (score, name)

    conn = connect_DB()
    c = conn.cursor()
    c.execute(query, val)    
    conn.commit()
    conn.close()


def update_High_Score(name, score, hscore):
    query = "UPDATE tb_scores SET last_score = %s, high_score = %s WHERE pl_name = %s"
    val = (score, hscore, name)

    conn = connect_DB()
    c = conn.cursor()
    c.execute(query, val)    
    conn.commit()
    conn.close()



def reg_Score(player_name, score):
    # verifica se o jogador já tem pontuação registrada
    s = select(player_name)
    if s:
        # verifica se o score atual é maior que o seu próprio recorde
        if score > s[0][2]:
            update_High_Score(player_name, score, score)
        else:
            update_Score(player_name, score)
    else:
        insert(player_name, score, score)

        


for i in select_all():
    print(i)