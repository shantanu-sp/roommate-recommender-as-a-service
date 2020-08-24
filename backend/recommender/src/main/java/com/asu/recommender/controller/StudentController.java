package com.asu.recommender.controller;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.http.client.HttpComponentsClientHttpRequestFactory;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import com.asu.recommender.constants.RecommenderConstants;
import com.asu.recommender.model.StudentPreference;
import com.asu.recommender.repo.StudentRepo;
import com.asu.recommender.service.StudentRecommenderService;

@RestController
@RequestMapping("/student")
public class StudentController {

	@Autowired
	StudentRepo repo;
	
	@Autowired
	StudentRecommenderService service;
	
	@CrossOrigin
	@PostMapping("/register")
	public List<StudentPreference> register(@RequestBody StudentPreference student) {
		if(student!=null) {
			repo.save(student);
		}
		// pythonClient.getKMeansOp(student);
		List<StudentPreference> filteredStudents =  service.recommend(student.getMinrent(), student.getMaxrent());
		List<StudentPreference> ret = new ArrayList<StudentPreference>();
		ret = filteredStudents;
		
		if (ret.contains(student)){
			ret.remove(student);
		}
		return ret;
		
	}
	
	@RequestMapping(value="/db/{id}")
	public StudentPreference queryDB(@PathVariable("id") Long id){
		
		return repo.findById(id).orElse(null);
	}
	
	
	@CrossOrigin
	@RequestMapping("/getPreferences/{knn}")
	public StudentPreference[] testClient(@RequestBody StudentPreference student,@PathVariable("knn") Long knn){
		HttpComponentsClientHttpRequestFactory clientRequestFactory = new HttpComponentsClientHttpRequestFactory();
		clientRequestFactory.setConnectionRequestTimeout(0);
		clientRequestFactory.setReadTimeout(0);
		RestTemplate restTemplate = new RestTemplate(clientRequestFactory);
		
		if(student!=null && knn > 0) {
		repo.save(student);
		System.out.println(knn);
		
		Long studentId = student.getId();
		String pythonServiceUrl = RecommenderConstants.pythonServiceURL;
		pythonServiceUrl = pythonServiceUrl + "/" + Long.toString(studentId);
		pythonServiceUrl = pythonServiceUrl + "/" + Long.toString(knn);
		ResponseEntity<StudentPreference[]> s = 
				restTemplate.getForEntity(pythonServiceUrl, StudentPreference[].class);
		StudentPreference[] s1 = s.getBody();
		
		for(int i =0;i<s1.length;i++) {
			System.out.println(s1[i].toString());
		}
		return s1;
		}
		return null;

	}
	
}
