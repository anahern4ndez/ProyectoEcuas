using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
//using System.Diagnostics;
using System.IO;
using UnityEditor;  
//using IronPython;  
//using IronPython.Modules;

public class CuatroPisos : MonoBehaviour {
	float[] piso1x;
	float[] piso2x;
	float[] piso3x;
    float[] piso4x;
    public bool moviendo = false;
	public GameObject hueso1;
	public GameObject hueso2;
	public GameObject hueso3;
	public GameObject hueso4;

	private Vector3 hueso1pos;
	private Vector3 hueso2pos;
	private Vector3 hueso3pos;
	private Vector3 hueso4pos;
	int contadorPos=0;

	private int N; //cantidad de datos
	// Use this for initialization
	void Start () {
		/* ejecucion de .py */


        // Display the file contents by using a foreach loop.

		string[] lines = System.IO.File.ReadAllLines("Assets/Py/four_floors.dat");
		N = lines.Length;
		piso1x = new float[lines.Length];
		piso2x = new float[lines.Length];
		piso3x = new float[lines.Length];
        piso4x = new float[lines.Length];
        int i =0;
        foreach (string line in lines)
        {
            // Use a tab to indent each line of the file.
			string[] sep;
			sep = line.Split();
            piso1x[i] = float.Parse(sep[1]);
			piso2x[i] = float.Parse(sep[2]);
			piso3x[i] = float.Parse(sep[3]);
            piso4x[i] = float.Parse(sep[4]);
            i++;
        }
		hueso1pos = hueso1.transform.position;
		hueso2pos = hueso2.transform.position;
		hueso3pos = hueso3.transform.position;
        hueso4pos = hueso4.transform.position;
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
            hueso4.transform.position = new Vector3(hueso4pos.x + piso4x[contadorPos], hueso4pos.y, hueso4pos.z);
            contadorPos++;
		}
	}
}
