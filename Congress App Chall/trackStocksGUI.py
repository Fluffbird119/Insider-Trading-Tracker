import pygame
from trackStocks import set_up, purchased_most, find_index, how_much_one_purchase
from key_code_finder import find_keycode, find_numcode
import os

# conditions list
# 


screen_size_x = 800
screen_size_y = 455

pygame.init()
screen = pygame.display.set_mode((screen_size_x,screen_size_y))
pygame.display.set_caption("Insider Trading Tracker")

# pygame.draw.rect(screen, color, pygame.Rect(x1,y1,width,height))

run = True

search_name = ""
year_set2 = ""
year_set = ""
person = ""
in_person_search_text_box = False
in_year_set_box = False
counterNum = 0
alternateCounter = 0
icon_color = "black"
offset_counter_person = 0
offset_counter_year = 0
can_PM = False
can_SS = False
can_draw = False
in_PM_search_box = False
offset_y = 35
offset_x = -100
font_directory = "Congress App Chall/Data/roboto/Roboto-Regular.ttf"



while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # finds mouse position
        (mouse_x, mouse_y) = pygame.mouse.get_pos()

        background_color = pygame.Color(200, 249, 249)
        screen.fill(background_color)

        # SS person search box
        text_box_color = pygame.Color(249, 246, 238)
        pygame.draw.rect(screen, text_box_color, pygame.Rect(50,45 + offset_y,400,35)) # use more vars for these next time idiot

        # SS year search box
        pygame.draw.rect(screen, text_box_color, pygame.Rect(50,105 + offset_y,100,35))

        # PM year search box
        pygame.draw.rect(screen, text_box_color, pygame.Rect(600 + offset_x,45 + offset_y,120,35))

        font = pygame.font.Font(font_directory, 20)

        Last_first_description = font.render("Last, First", True, "black")
        textRect = Last_first_description.get_rect()
        screen.blit(Last_first_description, (50, 22 + offset_y))

        year_description = font.render("Year", True, "black")
        textRect = year_description.get_rect()
        screen.blit(year_description, (50, 83 + offset_y))

        output_text_description = font.render("Output", True, "black")
        textRect = output_text_description.get_rect()
        screen.blit(output_text_description, (50, 160 + offset_y))

        PM_year_description = font.render("Year", True, "black")
        textRect = PM_year_description.get_rect()
        screen.blit(PM_year_description, (600 + offset_x, 23 + offset_y))


        font = pygame.font.Font(font_directory, 32)

        what_is_SS = font.render("Specific Search", True, "black")
        textRect = what_is_SS.get_rect()
        screen.blit(what_is_SS, (50, -25 + offset_y))

        # what_is_PM = font.render("Purchased", True, "black")
        # textRect = what_is_PM.get_rect()
        # screen.blit(what_is_PM, (600, -50 + offset_y))

        what_is_PM2 = font.render("Purchased Most", True, "black")
        textRect = what_is_PM2.get_rect()
        screen.blit(what_is_PM2, (600 + offset_x, -25 + offset_y))

        # PM search button
        # pygame.draw.rect(screen, text_box_color, pygame.Rect(600,105,175,175))

        # commented out icon blinking code #* note event based programing messes this up so no use
        # dont wanna delete cuz it took so long to make :(
        """
        # blinking icon
        # if alternateCounter == 0:
        #     if in_person_search_text_box == True:
        #         for k in range(len(search_name)):
        #             if k != 0:
        #                 offset_counter_person += 16
        #             elif k == 0:
        #                 offset_counter_person += 20
        #         pygame.draw.rect(screen, icon_color, pygame.Rect(77 + offset_counter_person,47,5,30))
        #         offset_counter_person = 0

        #     elif in_year_set_box == True:
        #         for k in range(len(search_name)):
        #             if k != 0:
        #                 offset_counter_person += 16
        #             elif k == 0:
        #                 offset_counter_person += 20
        #         pygame.draw.rect(screen, icon_color, pygame.Rect(77 + offset_counter_year,107,5,30))
        #         offset_counter_person = 0

        # elif alternateCounter == 1:
        #     if in_person_search_text_box == True:
        #         for k in range(len(search_name)):
        #             if k != 0:
        #                 offset_counter_person += 16
        #             elif k == 0:
        #                 offset_counter_person += 20
        #         pygame.draw.rect(screen, icon_color, pygame.Rect(77 + offset_counter_person,47,5,30))
        #         offset_counter_person = 0

        #     elif in_year_set_box == True:
        #         for k in range(len(search_name)):
        #             if k != 0:
        #                 offset_counter_person += 16
        #             elif k == 0:
        #                 offset_counter_person += 20
        #         pygame.draw.rect(screen, icon_color, pygame.Rect(77 + offset_counter_year,107,5,30))
        #         offset_counter_person = 0
        """

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if in_person_search_text_box == True and search_name != "":
                    temp_search_name = ""
                    split_search_name = list(search_name)
                    end_of_string = len(split_search_name) - 1
                    split_search_name.pop(end_of_string)
                    search_name = ''.join(split_search_name)
                elif in_year_set_box == True and year_set != "":
                    temp_year_set = ""
                    split_year_set = list(year_set)
                    end_of_nums = len(split_year_set) - 1
                    split_year_set.pop(end_of_nums)
                    year_set = ''.join(split_year_set)
                elif in_PM_search_box == True and year_set2 != "":
                    temp_year_set2 = ""
                    split_year_set2 = list(year_set2)
                    end_of_string = len(split_year_set2) - 1
                    split_year_set2.pop(end_of_string)
                    year_set2 = ''.join(split_year_set2)
            
            elif event.key == pygame.K_RETURN:
                if in_PM_search_box == False:
                    in_person_search_text_box = True
                    organized_FD = set_up(year)
                    index = find_index(organized_FD, person)
                    total_purchased = how_much_one_purchase(organized_FD, year, index, person)
                    splitPerson = person.split(",")

                    enter_pressed = False
                    can_SS = True
                    hit_search_button = True

                    if len(year) == 4:
                        can_draw = True
                    else:
                        can_draw = False
                elif in_PM_search_box == True:
                    in_PM_search_box = True
                    in_person_search_text_box = False
                    organized_FD = set_up(year2)
                    PMP_person_and_PMP_num = purchased_most(organized_FD,year2)
                    
                    PMP_person = PMP_person_and_PMP_num[0]

                    PMP_num = PMP_person_and_PMP_num[1]

                    split_PMP_person = PMP_person.split(",")

                    can_PM = True
                    hit_search_button = True
                    
                    if len(year2) == 4:
                        can_draw = True
                    else:
                        can_draw = False
            
            elif event.key == pygame.K_ESCAPE:
                run = False

            else:
                if in_person_search_text_box == True:
                    next_letter = find_keycode(event.key)
                    search_name += next_letter 
                    search_name = search_name.title()
                elif in_year_set_box == True: 
                    next_num = find_numcode(event.key)
                    year_set += next_num
                elif in_PM_search_box == True:
                    next_letter2 = find_numcode(event.key)
                    year_set2 += next_letter2 
        
        if len(year_set) == 4:
            year = year_set
            person = search_name
        if len(year_set2) == 4:
            year2 = year_set2
        
        font = pygame.font.Font(font_directory, 32)

        person_search = font.render(search_name, True, "black")
        textRect = person_search.get_rect()
        screen.blit(person_search, (50, 43 + offset_y))

        year_set_text = font.render(year_set, True, "black")
        textRect = year_set_text.get_rect()
        screen.blit(year_set_text, (50, 105 + offset_y))

        PM_set_text = font.render(year_set2, True, "black")
        textRect = PM_set_text.get_rect()
        screen.blit(PM_set_text, (600 + offset_x, 43 + offset_y))


        if event.type == pygame.MOUSEBUTTONDOWN:
            # person search box
            if mouse_x >= 50 and mouse_x <= 410 and mouse_y >= 45 + offset_y and mouse_y <= 80 + offset_y:
                in_person_search_text_box = True
                in_year_set_box = False
                in_PM_search_box = False
            elif mouse_x >= 600 + offset_x and mouse_x <= 685 + offset_x and mouse_y >= 45 + offset_y and mouse_y <= 80 + offset_y:
                in_PM_search_box = True
                in_person_search_text_box = False
                in_year_set_box = False 
            elif mouse_x > 415 and mouse_x <= 450 and mouse_y >= 45 + offset_y and mouse_y <= 80 + offset_y:
                in_PM_search_box = False
                in_person_search_text_box = True
                organized_FD = set_up(year)
                index = find_index(organized_FD, person)
                total_purchased = how_much_one_purchase(organized_FD, year, index, person)
                splitPerson = person.split(",")

                enter_pressed = False
                can_SS = True
                hit_search_button = True

                if len(year) == 4:
                    can_draw = True
                else:
                    can_draw = False
            
            elif mouse_x > 685 + offset_x and mouse_x < 720 + offset_x and mouse_y >= 45 + offset_y and mouse_y <= 80 + offset_y:
                in_PM_search_box = True
                in_person_search_text_box = False
                organized_FD = set_up(year2)
                PMP_person_and_PMP_num = purchased_most(organized_FD,year2)
                
                PMP_person = PMP_person_and_PMP_num[0]

                PMP_num = PMP_person_and_PMP_num[1]

                split_PMP_person = PMP_person.split(",")

                can_PM = True
                hit_search_button = True
                
                if len(year2) == 4:
                    can_draw = True
                else:
                    can_draw = False

            # year set box
            elif mouse_x >= 50 and mouse_x <= 170 and mouse_y >= 105 + offset_y and mouse_y <= 140 + offset_y:
                in_year_set_box = True
                in_person_search_text_box = False
        
        # box for output to be in
        pygame.draw.rect(screen, text_box_color, pygame.Rect(50,185 + offset_y,700,195))
        
        if person == "" and in_PM_search_box == False:
            can_draw = False
        if can_draw == True:
            # purposefully making my code more inefficent lol
            if in_person_search_text_box == True and can_SS == True:
                full_text = ""
                full_text2 =""
                full_text3 = ""

                # redundant
                if organized_FD[index][0] != "Prefix":
                    full_text += organized_FD[index][0]

                full_text += splitPerson[1] + " "
                full_text += splitPerson[0] + " "
                full_text += "purchased"
                full_text2 += "stocks "
                full_text2 += str(total_purchased)
                full_text2 += " times in "
                full_text2 += str(year)
                # full_text += " and can be found "
                # full_text += str(index)
                # full_text += " lines from the top "

                can_SS = False

            elif in_PM_search_box == True and can_PM == True:
                full_text = ""
                full_text2 = ""
                full_text3 = ""

                full_text += split_PMP_person[1] + " "
                full_text += split_PMP_person[0]
                full_text += " purchased "
                full_text2 += " " + str(PMP_num)
                full_text2 += " times in "
                full_text2 += str(year2)
                full_text2 += " which is" 
                full_text3 += " the most in that year"

                can_PM = False

            # box for output to be in
            # pygame.draw.rect(screen, text_box_color, pygame.Rect(75,185,650,195))

            font = pygame.font.Font(font_directory,40)
            data_output = font.render(full_text, True, "black")
            textRect = data_output.get_rect()
            screen.blit(data_output, (75, 195 + offset_y))

            # technically bad code but who cares
            data_output = font.render(full_text2, True, "black")
            textRect = data_output.get_rect()
            screen.blit(data_output, (75, 255 + offset_y))

            data_output = font.render(full_text3, True, "black")
            textRect = data_output.get_rect()
            screen.blit(data_output, (75, 315 + offset_y))

            # mouse_x_pos = font.render("mouse x" + str(mouse_x), True, "black")
            # textRect = mouse_x_pos.get_rect()
            # screen.blit(mouse_x_pos, (400, 305))

            # mouse_y_pos = font.render("mouse y" + str(mouse_y), True, "black")
            # textRect = mouse_y_pos.get_rect()
            # screen.blit(mouse_y_pos, (400, 360))
            
            
            
        # search icons
        spyglass_image_for_person = pygame.image.load("Congress App Chall/Data/Search Icon.png").convert_alpha()
        DEFAULT_IMAGE_SIZE = (155,95)
        spyglass_image_for_person = pygame.transform.scale(spyglass_image_for_person, DEFAULT_IMAGE_SIZE)
        screen.blit(spyglass_image_for_person, (355,17 + offset_y))

        spyglass_image_for_person2 = pygame.image.load("Congress App Chall/Data/Search Icon.png").convert_alpha()
        DEFAULT_IMAGE_SIZE = (155,95)
        spyglass_image_for_person = pygame.transform.scale(spyglass_image_for_person, DEFAULT_IMAGE_SIZE)
        screen.blit(spyglass_image_for_person, (625 + offset_x,17 + offset_y))

        pygame.display.flip()
    
    # counterNum += 1
            
    # if counterNum == 2500000:
    #     if alternateCounter == 0:
    #         icon_color = "black"
    #         alternateCounter = 1

    #     elif alternateCounter == 1:
    #         icon_color = text_box_color
    #         alternateCounter = 0

    #     print(counterNum)
    #     counterNum = 0