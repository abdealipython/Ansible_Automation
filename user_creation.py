---
- hosts: localhost
  gather_facts: no
  become: yes
  tasks:
    - name: Create 'three' group
      group:
        name: three
        state: present

    - name: Create 'other' group
      group:
        name: other
        state: present

    - name: Create user accounts
      user:
        name: "harman{{ item }}"
        groups: "{{ 'three' if (item|int % 3) == 0 else 'other' }}"
        state: present
      loop: "{{ range(1, 16) | list }}"
