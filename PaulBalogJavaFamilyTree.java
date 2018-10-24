import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class PaulBalogFamilyTree {

	public static void main(String[] args) {

		// E <name1> <name2> or E <name1> <name2> <name3>
		// Name1 marries Name2. Name1 marries Name2 and has Name3.
		// X <name1> <relation> <name2>
		// Is name1 related as a child/spouse/sibling/ancestor/cousin/unrelated to
		// name2.
		// W <relation> <name1>
		// List all people related as a child/spouse/sibling/ancestor/cousin/unrelated
		// to name2.

		Interpretor familyTree = new Interpretor();
		BufferedReader buffin = new BufferedReader(new InputStreamReader(System.in));
		while (true) {
			String input = null;
			try {
				input = buffin.readLine();
			} catch (IOException e) {
				return;
			}
			String[] words = new String[4];
			words = input.split(" ");
			switch (words[0]) {
			case "E":
				if (words[3] == null)
					familyTree.marry(words[1], words[2]);
				else
					familyTree.bearchild(words[1], words[2], words[3]);
				break;
			case "W":
				System.out.println(input);
				Iterator<Person> peopleList = familyTree.allRelatedSorted(words[1], words[2]).iterator();
				while (peopleList.hasNext())
					System.out.println(peopleList.next());
				System.out.println();
				break;
			case "X":
				System.out.println(input);
				boolean inRelation = familyTree.relation(words[1], words[2], words[3]);
				if (inRelation == true)
					System.out.println("Yes");
				else
					System.out.println("No");
				System.out.println();
				break;
			}
		}
	}
}

class Person implements Comparable<Person> {

	// Every person has a name, a list of their spouses, their biological parents,
	// and their children.

	String name;
	ArrayList<Person> spouses = new ArrayList<Person>();
	Person parent1;
	Person parent2;
	ArrayList<Person> children = new ArrayList<Person>();

	public Person(String name) {
		this.name = name;
	}

	public void addSpouse(Person person) {
		spouses.add(person);
	}

	public void setParent1(Person person) {
		parent1 = person;
	}

	public void setParent2(Person person) {
		parent2 = person;
	}

	public void addChild(Person person) {
		children.add(person);
	}

	@Override
	public int compareTo(Person person) {
		return (name.compareTo(person.name));
	}

	public String toString() {
		return name;
	}

}

class WhoIs {

	// Private functions are helper functions

	// Removes duplicate entries in ArrayLists using just ArrayLists. O(n^2)? oof

	private ArrayList<Person> clearDuplicates(ArrayList<Person> arrayPersons) {
		ArrayList<Person> noDuplicates = new ArrayList<Person>();
		for (Person person : arrayPersons) {
			if (!noDuplicates.contains(person))
				noDuplicates.add(person);
		}
		return noDuplicates;
	}

	// You can directly fetch a person's children, spouses, and parents

	public ArrayList<Person> children(Person person) {
		ArrayList<Person> children = new ArrayList<Person>();
		children.addAll(person.children);
		children = clearDuplicates(children);
		return children;
	}

	public ArrayList<Person> spouses(Person person) {
		ArrayList<Person> spouses = new ArrayList<Person>();
		spouses.addAll(person.spouses);
		spouses = clearDuplicates(spouses);
		return spouses;
	}

	public ArrayList<Person> siblings(Person person) {
		ArrayList<Person> siblings = new ArrayList<Person>();
		siblings.addAll(person.parent1.children);
		siblings.addAll(person.parent2.children);
		siblings = clearDuplicates(siblings);
		siblings.removeAll(Collections.singleton(person));
		return siblings;

	}

	// Ancestors, descendants, cousins, related, and unrelated require recursion

	// Ancestors are anyone that be *directly* related to you (i.e. grandparents,
	// grandchildren)
	// Cousins would share common ancestors, but would not be direct ancestors.
	// (i.e. aunts, nephews)

	public ArrayList<Person> ancestors(Person person) {
		ArrayList<Person> ancestors = new ArrayList<Person>();
		if (person.parent1 != null) {
			ancestors.add(person.parent1);
			ancestors.add(person.parent2);
			ancestors.addAll(ancestors(person.parent1));
			ancestors.addAll(ancestors(person.parent2));
		} else
			return ancestors;
		ancestors = clearDuplicates(ancestors);
		return ancestors;

	}

	// This is your children, and their children, and so on.
	// This *might* be unnecessary. Maybe. It's here for completion's sake.

	private ArrayList<Person> descendants(Person person) {
		ArrayList<Person> descendants = new ArrayList<Person>();
		ArrayList<Person> nextDescendants = new ArrayList<Person>();
		if (person.children != null) {
			descendants.addAll(person.children);
			for (Person target : descendants) {
				nextDescendants.addAll(descendants(target));
			}
		}

		nextDescendants.addAll(descendants);
		nextDescendants = clearDuplicates(nextDescendants);
		return nextDescendants;
	}

	// This is everyone you do not share a direct line with, are not your parents,
	// children, or yourself.
	// Cousins would share common ancestors, but would not be direct ancestors.
	// Descendant of Ancestors - Exclusions = Cousins.

	public ArrayList<Person> cousins(Person person) {
		ArrayList<Person> ancestors = new ArrayList<Person>();
		ArrayList<Person> cousins = new ArrayList<Person>();
		ancestors.addAll(ancestors(person));
		Iterator<Person> ancestorsList = ancestors.iterator();
		while (ancestorsList.hasNext()) {
			ArrayList<Person> descendantPeople = new ArrayList<>(descendants(ancestorsList.next()));
			cousins.addAll(descendantPeople);
		}

		ArrayList<Person> exclusions = new ArrayList<Person>();
		exclusions.add(person);
		exclusions.add(person.parent1);
		exclusions.add(person.parent2);
		exclusions.addAll(person.children);
		exclusions = clearDuplicates(exclusions);
		cousins = clearDuplicates(cousins);
		cousins.removeAll(exclusions);
		return cousins;
	}

	// This is everyone you can be connected with.
	// Ancestors + Cousins + Inclusions + Descendants - Self = Related.

	private ArrayList<Person> related(Person person) {
		ArrayList<Person> related = new ArrayList<Person>();
		related.addAll(ancestors(person));
		related.addAll(cousins(person));
		related.addAll(descendants(person));

		ArrayList<Person> inclusions = new ArrayList<Person>();
		inclusions.add(person.parent1);
		inclusions.add(person.parent2);
		inclusions.addAll(person.children);
		related.addAll(inclusions);
		related.removeAll(Collections.singleton(person));
		related = clearDuplicates(related);
		return related;
	}

	// This is everyone you're not connected with.
	// All - Related = Unrelated.

	public ArrayList<Person> unrelated(Person person, ArrayList<Person> people) {
		ArrayList<Person> unrelated = new ArrayList<Person>();
		unrelated.addAll(people);
		ArrayList<Person> related = new ArrayList<Person>();
		related.addAll(related(person));
		unrelated.removeAll(related);
		unrelated = clearDuplicates(unrelated);
		return unrelated;
	}
}

class Interpretor {

	// E <name1> <name2> or E <name1> <name2> <name3>
	// Name1 marries Name2. Name1 marries Name2 and has Name3.
	// X <name1> <relation> <name2>
	// Is name1 related as a child/spouse/sibling/ancestor/cousin/unrelated to
	// name2.
	// W <relation> <name1>
	// List all people related as a child/spouse/sibling/ancestor/cousin/unrelated
	// to name2.

	ArrayList<Person> people = new ArrayList<Person>();

	/* Tested Functions, not part of code.
	 * 
	 * Person findPerson(Person target, ArrayList<Person> people) { for (Person
	 * person : people) { if (person.name.equals(target.name)) return target; }
	 * return null; }
	 * 
	 * Person findPersonByName(String name, ArrayList<Person> people) { for (Person
	 * person : people) { if (person.name.equals(name)) return person; } return
	 * null; }
	 * 
	 */

	int findPersonIndexByName(String name, ArrayList<Person> people) {
		for (Person person : people) {
			if (person.name.equals(name))
				return people.indexOf(person);
		}
		return -1;
	}

	// E <name1> <name2> or E <name1> <name2> <name3>
	// Name1 marries Name2. Name1 marries Name2 and has Name3.

	void bearchild(String name1, String name2, String name3) {
		// We're assuming all children have married parents at the time
		marry(name1, name2);
		// We're assuming adoption is possible
		Person person3 = null;
		int person3index = findPersonIndexByName(name3, people);
		if (person3index == -1) {
			person3 = new Person(name3);
		} else {
			person3 = people.get(person3index);
		}
		Person person1 = people.get(findPersonIndexByName(name1, people));
		Person person2 = people.get(findPersonIndexByName(name2, people));
		person1.addChild(person3);
		person2.addChild(person3);
		person3.parent1 = person1;
		person3.parent2 = person2;
		if (person3index == -1) {
			people.add(person3);
		}
	}

	void marry(String name1, String name2) {
		Person person1 = null;
		Person person2 = null;
		int person1index = findPersonIndexByName(name1, people);
		int person2index = findPersonIndexByName(name2, people);
		if (person1index == -1) {
			person1 = new Person(name1);
		} else {
			person1 = people.get(person1index);
		}
		if (person2index == -1) {
			person2 = new Person(name2);
		} else {
			person2 = people.get(person2index);
		}
		person2.addSpouse(person1);
		person1.addSpouse(person2);
		if (person1index == -1) {
			people.add(person1);
		}
		if (person2index == -1) {
			people.add(person2);
		}
	}

	// X <name1> <relation> <name2>
	// Is name1 the child/spouse/sibling/ancestor/cousin/unrelated of name2?

	boolean relation(String name1, String relation, String name2) {
		WhoIs whois = new WhoIs();
		Person person = people.get(findPersonIndexByName(name2, people));
		ArrayList<Person> relatedList = new ArrayList<Person>();
		switch (relation) {
		case "child":
			relatedList.addAll(whois.children(person));
			break;
		case "spouse":
			relatedList.addAll(whois.spouses(person));
			break;
		case "sibling":
			relatedList.addAll(whois.siblings(person));
			break;
		case "ancestor":
			relatedList.addAll(whois.ancestors(person));
			break;
		case "cousin":
			relatedList.addAll(whois.cousins(person));
			break;
		case "unrelated":
			relatedList.addAll(whois.unrelated(person, people));
			break;
		}
		for (Person personOnList : relatedList) {
			if (personOnList.name.equals(name1))
				return true;
		}
		return false;
	}

	ArrayList<Person> allRelatedSorted(String relation, String name1) {
		WhoIs whois = new WhoIs();
		Person person = people.get(findPersonIndexByName(name1, people));
		ArrayList<Person> relatedList = new ArrayList<Person>();
		switch (relation) {
		case "child":
			relatedList.addAll(whois.children(person));
			break;
		case "spouse":
			relatedList.addAll(whois.spouses(person));
			break;
		case "sibling":
			relatedList.addAll(whois.siblings(person));
			break;
		case "ancestor":
			relatedList.addAll(whois.ancestors(person));
			break;
		case "cousin":
			relatedList.addAll(whois.cousins(person));
			break;
		case "unrelated":
			relatedList.addAll(whois.unrelated(person, people));
			break;
		}

		Collections.sort(relatedList);

		return relatedList;
	}
}
