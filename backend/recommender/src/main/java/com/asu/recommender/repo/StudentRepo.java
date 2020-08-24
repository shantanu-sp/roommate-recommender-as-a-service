package com.asu.recommender.repo;

import java.util.List;
import java.util.Optional;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.asu.recommender.model.StudentPreference;
import java.lang.Long;

@Repository
public interface StudentRepo extends CrudRepository<StudentPreference,Long>{

	Optional<StudentPreference> findById(Long id);
	
	List<StudentPreference> findByMinrentLessThanEqual(Long maxRent);
	List<StudentPreference> findByMaxrentGreaterThanEqual(Long minRent);	
	
	
}
