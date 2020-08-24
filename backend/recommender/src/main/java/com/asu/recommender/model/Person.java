package com.asu.recommender.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name="person")
public class Person {

	@Id
	@GeneratedValue			//(strategy = GenerationType.SEQUENCE)
	private Long id;
	private String name;
	private Long minrent;
	private Long maxrent;
	
	public Long getId() {
		return id;
	}
	public void setId(Long id) {
		this.id = id;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public Long getMinrent() {
		return minrent;
	}
	public void setMinrent(Long minrent) {
		this.minrent = minrent;
	}
	public Long getMaxrent() {
		return maxrent;
	}
	public void setMaxrent(Long maxrent) {
		this.maxrent = maxrent;
	}
	@Override
	public String toString() {
		return "Person [id=" + id + ", name=" + name + ", minrent=" + minrent + ", maxrent=" + maxrent + "]";
	}
	
}