import pandas as pd

import snowflake.connector as snow

class SNOW():

    def execute(ID, DATABASE, WAREHOUSE, SQL):

        try:

            # Establishing the connection

            ctx = snow.connect(

                authenticator='externalbrowser',

                user=ID,  # CHANGE USER

                host="###############",

                account="#################",

                database=DATABASE, ## CHANGE DATABASE

                warehouse=WAREHOUSE, ## CHANGE WAREHOUSE

              ## Add Aditional Paramaters Here ##

                login_timeout=60,

                network_timeout=30,

                socket_timeout=10

            )

            # EXECUTE THE QUERRY

            with ctx.cursor() as cursor:

                cursor.execute(SQL)

                # Fetching the results into a DataFrame

                columns = [col[0] for col in cursor.description]

                data = cursor.fetchall()

                df = pd.DataFrame(data, columns=columns)

                print(df)

            return df


        except Exception as e:

            print(f"An error occurred: {e}")

        finally:

            ctx.close()  # Ensure the connection is closed
          

#---Run Code Example---#
sql_1 = """

    SELECT

        a.MATERIAL,

        a.ITEM_BASE_UOM AS BASE_UOM,

        a.LISTPRICEPER AS LIST_PRICE_PER
        
    FROM

        EXAMPLE AS a

    WHERE 

        a.LISTPRICEPER IS NOT NULL

"""

SNOW.execute("#####", "#####", "#####", sql_1)
