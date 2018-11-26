using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
//using System.Diagnostics;
using System.IO;
using UnityEditor;  
//using IronPython;  
//using IronPython.Modules;

public class TresPisos : MonoBehaviour {
	float[] piso1x;
	float[] piso2x;
	float[] piso3x;
	public bool moviendo = false;
	public GameObject hueso1;
	public GameObject hueso2;
	public GameObject hueso3;
	private Vector3 hueso1pos;
	private Vector3 hueso2pos;
	private Vector3 hueso3pos;
	int contadorPos=0;

	private int N; //cantidad de datos
	// Use this for initialization
	void Start () {
		/* ejecucion de .py */


        // Display the file contents by using a foreach loop.

		string[] lines = System.IO.File.ReadAllLines("Assets/Py/three_floors.dat");
		N = lines.Length;
		piso1x = new float[lines.Length];
		piso2x = new float[lines.Length];
		piso3x = new float[lines.Length];
		int i =0;
        foreach (string line in lines)
        {
            // Use a tab to indent each line of the file.
			string[] sep;
			sep = line.Split();
            piso1x[i] = float.Parse(sep[0]);
			piso2x[i] = float.Parse(sep[1]);
			piso3x[i] = float.Parse(sep[2]);
			i++;
        }
		hueso1pos = hueso1.transform.position;
		hueso2pos = hueso2.transform.position;
		hueso3pos = hueso3.transform.position;
		StartCoroutine ("CorutinaUpdatePos");

		
	}
	
	// Update is called once per frame
	void Update () {
	}


	IEnumerator CorutinaUpdatePos() {
		while (moviendo && (contadorPos<N)) {
			yield return new WaitForSeconds(0.1f);
			hueso1.transform.position = new Vector3(hueso1pos.x+ piso1x[contadorPos], hueso1pos.y, hueso1pos.z);
			hueso2.transform.position = new Vector3(hueso2pos.x+ piso2x[contadorPos], hueso2pos.y, hueso2pos.z);
			hueso3.transform.position = new Vector3(hueso3pos.x+ piso3x[contadorPos], hueso3pos.y, hueso3pos.z);
			contadorPos++;
		}
	}
}
