package com.asu.recommender;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.asu.recommender.model.Person;
import com.asu.recommender.repo.PersonRepo;

@RestController
@SpringBootApplication
//@ComponentScan(basePackageClasses = {PersonRepo.class})
public class RecommenderApplication {

	@Autowired
	PersonRepo repo;

	public static void main(String[] args) {
		SpringApplication.run(RecommenderApplication.class, args);
	}

	@GetMapping("/")
    public String hello() {
            return "Hello Spring Boot!";
    }

	@RequestMapping(value="/db/{id}")
	public Person queryDB(@PathVariable("id") Long id){
		return repo.findById(id).orElse(null);
	}
	
	@PostMapping("/register")
	public void register(@RequestBody Person person) {
		if(person!=null) {
			repo.save(person);
		}
		
	}
	
	@GetMapping("/getRecommend/{minrent}/{maxrent}")
    public List<Person> recommend(@PathVariable("minrent") Long minRent, 
    		@PathVariable("maxrent") Long maxRent) {
			List<Person> a = repo.findByMinrentLessThanEqual(maxRent);
			List<Person> b = repo.findByMaxrentGreaterThanEqual(minRent);
			List<Person> ret = new ArrayList<Person>();
			for(Person p : a) {
				if(b.contains(p)) {
					ret.add(p);
				}
				
			}
			System.out.println(a.size());
			System.out.println("#######");
			System.out.println(b.size());
            return ret;
    }
	
	
}
