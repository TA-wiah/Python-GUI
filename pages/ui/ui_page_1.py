import pyvisual as pv


def create_page_1_ui(window,ui):
    """
    Create and return UI elements for Page 1.
    :param container: The page widget for Page 1.
    :return: Dictionary of UI elements.
    """
    ui_page = {}
    ui_page["TextInput_0"] = pv.PvTextInput(container=window, x=54, y=103, width=200,
        height=40, background_color=(255, 255, 255, 1), is_visible=True, placeholder='User Name',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/BaiJamjuree/BaiJamjuree.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(0, 0, 0, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=10, icon_color='none',
        text_type='Text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["TextInput_1"] = pv.PvTextInput(container=window, x=54, y=162, width=200,
        height=40, background_color=(255, 255, 255, 1), is_visible=True, placeholder='Password',
        text_alignment='left', default_text='', paddings=(10, 0, 20, 0), font='assets/fonts/Roboto/Roboto.ttf',
        font_size=10, font_color=(0, 0, 0, 1), border_color=(0, 0, 0, 1), border_thickness=1,
        border_style="solid", corner_radius=0, box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', icon_path=None,
        icon_scale=1, icon_position='left', icon_spacing=0, icon_color='none',
        text_type='text', max_length=None, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["Button_2"] = pv.PvButton(container=window, x=54, y=270, width=200,
        height=50, text='Submit', font='assets/fonts/Poppins/Poppins.ttf', font_size=16,
        font_color=(255, 255, 255, 1), font_color_hover=None, bold=False, italic=False,
        underline=False, strikethrough=False, idle_color=(56, 136, 255, 1), hover_color=None,
        clicked_color=None, border_color=(100, 100, 100, 1), border_hover_color=None, border_thickness=0,
        corner_radius=25, border_style="solid", box_shadow='1px 2px 4px 0px rgba(0,0,0,0.2)', box_shadow_hover='0px 2px 4px 5px rgba(0,0,0,0.2)',
        icon_path=None, icon_position='left', icon_color=(255, 255, 255, 1), icon_color_hover=None,
        icon_spacing=0, icon_scale=1, paddings=(0, 0, 0, 0), is_visible=True,
        is_disabled=False, opacity=1, on_hover=None, on_click=None,
        on_release=None, tag=None)

    ui_page["Icon_3"] = pv.PvIcon(container=window, x=-1, y=-1, width=27,
        height=27, idle_color=(75, 75, 75, 1), preserve_original_colors=False, icon_path='assets/icons/f252c2c4ac.svg',
        corner_radius=0, flip_v=False, flip_h=False, rotate=0,
        border_color=None, border_hover_color=None, border_thickness=0, border_style="solid",
        on_hover=None, on_click=None, on_release=None, is_visible=True,
        opacity=1, tag=None)

    ui_page["Icon_4"] = pv.PvIcon(container=window, x=304, y=-1, width=400,
        height=400, idle_color=(12, 111, 123, 1), preserve_original_colors=True, icon_path='assets/icons/1836339339.svg',
        corner_radius=0, flip_v=False, flip_h=False, rotate=0,
        border_color=None, border_hover_color=None, border_thickness=0, border_style="solid",
        on_hover=None, on_click=None, on_release=None, is_visible=True,
        opacity=1, tag=None)

    ui_page["Text_5"] = pv.PvText(container=window, x=26, y=357, width=137,
        height=23, idle_color=(238, 225, 255, 0), text='New To Slayer?', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/Rubik/Rubik.ttf', font_size=13,
        font_color=(254, 254, 254, 1), bold=True, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Text_6"] = pv.PvText(container=window, x=154, y=358, width=61,
        height=20, idle_color=(230, 221, 239, 0), text='Sign Up', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/EBGaramond/EBGaramond.ttf', font_size=16,
        font_color=(91, 94, 166, 1), bold=False, italic=False, underline=True,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Checkbox_7"] = pv.PvCheckbox(container=window, x=52, y=219, width=145,
        height=35, text='Stay logged in', is_checked=True, checked_color=(214, 214, 214, 1),
        unchecked_color=(214, 214, 214, 1), checkmark_color=(0, 0, 0, 1), checkmark_size=12, checkbox_size=15,
        corner_radius=10, checkmark_type='✓', border_color=(0, 0, 0, 1), border_thickness=0,
        spacing=10, font='assets/fonts/Poppins/Poppins.ttf', font_size=14, font_color=(0, 0, 0, 1),
        bold=True, italic=False, underline=False, strikeout=False,
        paddings=(5, 0, 0, 0), is_visible=True, opacity=1, tag=None,
        on_change=None)

    ui_page["Text_8"] = pv.PvText(container=window, x=52, y=53, width=136,
        height=44, idle_color=(151, 94, 181, 0), text='Login', is_visible=True,
        text_alignment='left', paddings=(0, 0, 0, 0), font='assets/fonts/SourceCodePro/SourceCodePro.ttf', font_size=37,
        font_color=(255, 255, 255, 1), bold=True, italic=False, underline=False,
        strikethrough=False, opacity=1, border_color=None, corner_radius=0,
        on_hover=None, on_click=None, on_release=None, tag=None)

    ui_page["Rectangle_9"] = pv.PvRectangle(container=window, x=17, y=38, width=287,
        height=350, idle_color=None, border_color=(0, 0, 0, 1), border_thickness=2,
        corner_radius=10, border_style="solid", opacity=1, is_visible=True,
        on_hover=None, on_click=None, on_release=None, tag=None)

    return ui_page
