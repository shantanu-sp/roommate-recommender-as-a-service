package com.asu.recommender.repo;

import org.springframework.stereotype.Repository;

import com.asu.recommender.model.Person;

import org.springframework.data.repository.CrudRepository;
import java.lang.Long;
import java.util.Optional;
import java.util.List;

@Repository
public interface PersonRepo extends CrudRepository<Person,Long>{
	Optional<Person> findById(Long id);
	//Optional<Person> findByMinRentGreaterThan(Long minRent);
	//List<Person> findByMinrentGreaterThanEqual(Long minRent);
	//List<Person> findByMaxrentIsLessThanEqual(Long maxRent);
	
	List<Person> findByMinrentLessThanEqual(Long maxRent);
	List<Person> findByMaxrentGreaterThanEqual(Long minRent);
}

