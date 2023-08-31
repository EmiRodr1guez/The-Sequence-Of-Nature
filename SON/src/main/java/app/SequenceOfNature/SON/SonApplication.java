package app.SequenceOfNature.SON;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@SpringBootApplication
@Controller
public class SonApplication {

	public static void main(String[] args) {
		SpringApplication.run(SonApplication.class, args);
	}

	//Route for home page
	//Accepts POST request for that HTML form that's going to be carrying the audio file
	@PostMapping("/home")
	public String home() {
		return "index";
	}

	//Route for login page
	//Accepts POST request for that HTML form that's carrying user credentials
	@PostMapping("/login")
	public String login() {
		return "login";
	}

	//Route for account page
	//Library of songs they've analyzed is shown, with specific info for each song
	@RequestMapping("/account")
	public String account() {
		return "account";
	}

	//Route for about page
	//Explaining how the Program analyzes the song and how the frequency of a given song is determined
	//Everything we've learned in this project
	@RequestMapping("/about")
	public String about() {
		return "about";
	}

}
