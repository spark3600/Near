from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 14789064
    API_HASH = "0532c65daeaa8bed31350cb48eb5d78e"
    # the name to display in your alive message
    ALIVE_NAME = "Nikita"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://oatagmky:Brny5zrOEflngwOGFhdyF9-JWMR4_IR-@abul.db.elephantsql.com/oatagmky"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOHcBuxUj300i6g1jnx4HM4Pwch6XwDHtXcIpP872IUoyWeJvSQE7KodCmpUvEl5fs_4vO1PO8A9ItOg06dOHIGuxEJEEotmgTpFnlEWmwJn-7x9amjGO7c6Z4Iw6VOaGhbm60GTdAL-NhnM0hy2asUUS8yN8HRFTjL5wgfqX_LIffNotTTMQXyOZ5Px9Y4DiTo3OscG6woaa-SVrL_ye7j89IOo_G4TIRH95lp5KHHX4yIZRW9WZ7eF5Q_09bZQ9mWWwxfb5p7MY8RjrXDBuLNtwztbL9wmZDehjX2vTxll4sRW-_stYJH1mWAR9e08m_L2VIe0Fy6XBhX9a1LJQvbhPtVg="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5875833040:AAEU-G2OeuMu4n6RD18tZ3RKjcxdK-Ea7hQ"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001725309227
    # command handler
    COMMAND_HAND_LER = "."
    VCMODE = "False"
    VC_SESSION = "your 2nd id telethon session" #note don't use maim account to vc player
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/rishabhanand2/tha_plugins"
    #don't edit this 
    THANOSABUSE = "False"#don't edit this else error in 
