import pygame, States as st, Game_engine as ge

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('PokePy')
    screen = pygame.display.set_mode((800, 600))
    states = {"SPLASH": st.SplashScreen(),
              "BATTLE OPTIONS": st.BattleOptions(),
              "ATTACK OPTIONS": st.AttackOptions(),
              "BACKPACK": st.Backpack(),
              "POKEMON SELECTION": st.SelectPokemon()}
    game = ge.Game(screen, states, "SPLASH")
    game.run()
    pygame.quit()
