package com.asu.recommender.model;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name="studentrecommend")
public class StudentPreference {

	@Id
	@GeneratedValue			//(strategy = GenerationType.SEQUENCE)	
	private Long id;
	private String name;
	private Long age;
	private String gender;
	private String major;
	private String program;
	private String preferenceone;
	private String preferencetwo;
	private Long minrent;
	private Long maxrent;
	private String foodpreference;
	private String description;
	private String email;
	
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
	public Long getAge() {
		return age;
	}
	public void setAge(Long age) {
		this.age = age;
	}
	public String getGender() {
		return gender;
	}
	public void setGender(String gender) {
		this.gender = gender;
	}
	public String getMajor() {
		return major;
	}
	public void setMajor(String major) {
		this.major = major;
	}
	public String getProgram() {
		return program;
	}
	public void setProgram(String program) {
		this.program = program;
	}
	public String getPreferenceone() {
		return preferenceone;
	}
	public void setPreferenceone(String preferenceone) {
		this.preferenceone = preferenceone;
	}
	public String getPreferencetwo() {
		return preferencetwo;
	}
	public void setPreferencetwo(String preferencetwo) {
		this.preferencetwo = preferencetwo;
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
	public String getFoodpreference() {
		return foodpreference;
	}
	public void setFoodpreference(String foodpreference) {
		this.foodpreference = foodpreference;
	}
	public String getDescription() {
		return description;
	}
	public void setDescription(String description) {
		this.description = description;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	@Override
	public String toString() {
		return "StudentPreference [id=" + id + ", name=" + name + ", age=" + age + ", gender=" + gender + ", major="
				+ major + ", program=" + program + ", preferenceone=" + preferenceone + ", preferencetwo="
				+ preferencetwo + ", minrent=" + minrent + ", maxrent=" + maxrent + ", foodpreference=" + foodpreference
				+ ", description=" + description + ", email=" + email + "]";
	}

	
	
}
