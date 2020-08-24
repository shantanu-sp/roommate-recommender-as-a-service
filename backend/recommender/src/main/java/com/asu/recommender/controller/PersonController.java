package com.asu.recommender.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/recommender")
public class PersonController {

	@GetMapping("/info")
    public String hello() {
            return "Roommate Recommender!";
    }
	
}
