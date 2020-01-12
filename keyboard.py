from vk_api.keyboard import VkKeyboard
from vk_api.keyboard import VkKeyboardColor
from config import MESSAGE_KEYBOARD


class Keyboard:
    def keyboard_menu(self):
        keyboard = VkKeyboard()
        keyboard.add_button(MESSAGE_KEYBOARD['start_keyb_kontroler'], color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button(MESSAGE_KEYBOARD['start_keyb_settings'], color=VkKeyboardColor.PRIMARY)
        return keyboard.get_keyboard()

    def keyboard_controllers(self):
        keyboard = VkKeyboard()
        keyboard.add_button(MESSAGE_KEYBOARD['kontroler_keyb_dirty_stop'], color=VkKeyboardColor.DEFAULT)
        keyboard.add_button(MESSAGE_KEYBOARD['kontroler_keyb_clear_stop'], color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button(MESSAGE_KEYBOARD['kontroler_keyb_bus'], color=VkKeyboardColor.DEFAULT)
        keyboard.add_button(MESSAGE_KEYBOARD['kontroler_keyb_trolleybus'], color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button(MESSAGE_KEYBOARD['menu_keyb'], color=VkKeyboardColor.PRIMARY)
        return keyboard.get_keyboard()

    def keyboard_bus(self):
        keyboard = VkKeyboard()
        keyboard.add_button(MESSAGE_KEYBOARD['kontroler_keyb_bus_1'], color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button(MESSAGE_KEYBOARD['kontroler_keyb_bus_2'], color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button(MESSAGE_KEYBOARD['kontroler_keyb_bus_3'], color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button(MESSAGE_KEYBOARD['kontroler_keyb_bus_4'], color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button(MESSAGE_KEYBOARD['back_keyb'], color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(MESSAGE_KEYBOARD['menu_keyb'], color=VkKeyboardColor.PRIMARY)
        return keyboard.get_keyboard()

    def keyboard_bus_1(self):
        keyboard = VkKeyboard()
        keyboard.add_button('1', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('1А', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('2', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('2А', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('3', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('5', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('6', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('7', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('8', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('9', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('10', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('11', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('11А', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('12', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('12А', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('13', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('13А', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('14', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('15А', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('15Б', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button(MESSAGE_KEYBOARD['back_keyb'], color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(MESSAGE_KEYBOARD['menu_keyb'], color=VkKeyboardColor.PRIMARY)
        return keyboard.get_keyboard()

    def keyboard_bus_2(self):
        keyboard = VkKeyboard()
        keyboard.add_button('15В', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('16', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('17', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('18', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('19', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('20', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('21', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('21А', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('21Б', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('22', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('23', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('23А', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('23Б', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('24', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('24Б', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('25', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('26', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('27', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('27А', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('28', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button(MESSAGE_KEYBOARD['back_keyb'], color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(MESSAGE_KEYBOARD['menu_keyb'], color=VkKeyboardColor.PRIMARY)
        return keyboard.get_keyboard()

    def keyboard_bus_3(self):
        keyboard = VkKeyboard()
        keyboard.add_button('29', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('30', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('30А', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('31', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('32', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('33', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('34', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('35', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('36', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('37', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('37А', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('38', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('39', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('39А', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('39Б', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('40', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('41', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('42', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('43', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('44', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button(MESSAGE_KEYBOARD['back_keyb'], color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(MESSAGE_KEYBOARD['menu_keyb'], color=VkKeyboardColor.PRIMARY)
        return keyboard.get_keyboard()

    def keyboard_bus_4(self):
        keyboard = VkKeyboard()
        keyboard.add_button('44А', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('45', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('46', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('47', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('50', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button(MESSAGE_KEYBOARD['back_keyb'], color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(MESSAGE_KEYBOARD['menu_keyb'], color=VkKeyboardColor.PRIMARY)
        return keyboard.get_keyboard()

    def keyboard_trolley_buses(self):
        keyboard = VkKeyboard()
        keyboard.add_button('1', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('2', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('3', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('4', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('5', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('6', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('7', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('8', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('9', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button(MESSAGE_KEYBOARD['back_keyb'], color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(MESSAGE_KEYBOARD['menu_keyb'], color=VkKeyboardColor.PRIMARY)
        return keyboard.get_keyboard()

    def keyboard_help(self):
        keyboard = VkKeyboard()
        keyboard.add_button(MESSAGE_KEYBOARD['settings_keyb_time'], color=VkKeyboardColor.DEFAULT)
        keyboard.add_button(MESSAGE_KEYBOARD['settings_keyb_sort'], color=VkKeyboardColor.DEFAULT)
        keyboard.add_button(MESSAGE_KEYBOARD['settings_keyb_display'], color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button(MESSAGE_KEYBOARD['menu_keyb'], color=VkKeyboardColor.PRIMARY)
        return keyboard.get_keyboard()

    def keyboard_time(self):
        keyboard = VkKeyboard()
        keyboard.add_button('30 мин', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('1 час', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('1 час 30 мин', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('2 часа', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('2 часа 30 мин', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('3 часа', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('3 часа 30 мин', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('4 часа', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('4 часа 30 мин', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button('5 часа', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('5 часа 30 мин', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('6 часа', color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button(MESSAGE_KEYBOARD['menu_keyb'], color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(MESSAGE_KEYBOARD['menu_keyb'], color=VkKeyboardColor.PRIMARY)
        return keyboard.get_keyboard()

    def keyboard_sort(self):
        keyboard = VkKeyboard()
        keyboard.add_button(MESSAGE_KEYBOARD['settings_keyb_sort_inside_1'], color=VkKeyboardColor.DEFAULT)
        keyboard.add_button(MESSAGE_KEYBOARD['settings_keyb_sort_inside_2'], color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button(MESSAGE_KEYBOARD['menu_keyb'], color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(MESSAGE_KEYBOARD['menu_keyb'], color=VkKeyboardColor.PRIMARY)
        return keyboard.get_keyboard()

    def keyboard_display(self):
        keyboard = VkKeyboard()
        keyboard.add_button(MESSAGE_KEYBOARD['settings_keyb_display_inside_1'], color=VkKeyboardColor.DEFAULT)
        keyboard.add_button(MESSAGE_KEYBOARD['settings_keyb_display_inside_2'], color=VkKeyboardColor.DEFAULT)
        keyboard.add_line()
        keyboard.add_button(MESSAGE_KEYBOARD['menu_keyb'], color=VkKeyboardColor.PRIMARY)
        keyboard.add_button(MESSAGE_KEYBOARD['menu_keyb'], color=VkKeyboardColor.PRIMARY)
        return keyboard.get_keyboard()