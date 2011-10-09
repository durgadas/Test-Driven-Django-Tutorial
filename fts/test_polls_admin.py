from functional_tests import FunctionalTest, ROOT
from selenium.webdriver.common.keys import Keys

class TestPollsAdmin(FunctionalTest):

    def test_can_create_new_poll_via_admin_site(self):

        # Gertrude opens her web browser, and goes to the admin page
        self.browser.get(ROOT + '/admin/')

        # She sees the familiar 'Django administration' heading
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        # She types in her username and passwords and hits return
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('admin')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('adm1n')
        password_field.send_keys(Keys.RETURN)

        # She now sees a couple of hyperlink that says "Polls"
        polls_links = self.browser.find_elements_by_link_text('Polls')
        self.assertEquals(len(polls_links), 2)

        # The second one looks more exciting, so she clicks it
        polls_links[1].click()

        # She is taken to the polls listing page, which shows she has
        # no polls yet
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('0 polls', body.text)

        # She sees a link to 'add' a new poll, so she clicks it
        new_poll_link = self.browser.find_element_by_link_text('Add poll')
        new_poll_link.click()

        # She sees some input fields for "Question" and "Date published"
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Question:', body.text)
        self.assertIn('Date published:', body.text)

        # She types in an interesting question for the Poll
        question_field = self.browser.find_element_by_name('question')
        question_field.send_keys("How awesome is Test-Driven Development?")

        # She sets the date and time of publication - it'll be a new year's
        # poll!
        date_field = self.browser.find_element_by_name('pub_date_0')
        date_field.send_keys('01/01/12')
        time_field = self.browser.find_element_by_name('pub_date_1')
        time_field.send_keys('00:00')

        save_button = self.browser.find_element_by_css_selector("input[value='Save']")
        save_button.click()

        # She is returned to the "Polls" listing, where she can see her
        # new poll, listed as a clickable link
        new_poll_links = self.browser.find_elements_by_link_text(
                "How awesome is Test-Driven Development?"
        )
        self.assertEquals(len(new_poll_links), 1)


