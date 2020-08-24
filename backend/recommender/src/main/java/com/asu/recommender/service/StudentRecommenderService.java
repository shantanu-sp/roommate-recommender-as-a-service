package com.asu.recommender.service;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.asu.recommender.model.StudentPreference;
import com.asu.recommender.repo.StudentRepo;

@Service
public class StudentRecommenderService {

	@Autowired StudentRepo repo;
	
    public List<StudentPreference> recommend(Long minRent, Long maxRent) {
			List<StudentPreference> a = repo.findByMinrentLessThanEqual(maxRent);
			List<StudentPreference> b = repo.findByMaxrentGreaterThanEqual(minRent);
			List<StudentPreference> ret = new ArrayList<StudentPreference>();
			for(StudentPreference p : a) {
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
